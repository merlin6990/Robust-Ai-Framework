import json
import re
class RAFCodeGenerator:
    def __init__(self):
        self.non_operands = ['start','data','poison_statement','data_statement','model_statement','plot_statement','metric','json']
        self.operand_stack = []
        self.code_stack = []
        self.label_counter=0
        with open("./config/import.cg", "r", encoding="utf-8") as file:
            content = file.read()
        self.import_str=content
        self.data_code="";
        self.code=""
        self.used_json=False

    def generate_train_loop_code(self):
        if(self.used_json):
         with open('./config/hyper.json', 'r') as file:
            json_data = json.load(file)
         train_code = (f"device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n"
                      f"model = MLP().to(device)\n"
                      f"criterion = nn.{json_data["criterion"]}()\n"
                      f"optimizer = optim.{json_data["optimizer"]}(model.parameters(), lr=learning_rate)\n\n")
        else:
            train_code = (f"device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n"
                          f"model = MLP().to(device)\n"
                          f"criterion = nn.CrossEntropyLoss()\n"
                          f"optimizer = optim.Adam(model.parameters(), lr=learning_rate)\n\n")
        with open('./config/train_loop.cg', 'r') as file:
            data = file.read()
            train_code+=data
        return train_code+"\n\n\n"

    def create_new_label(self,target):
        return 'Target_Label' + target
    def create_layer_label(self):
        self.label_counter += 1
        return 'fc' + str(self.label_counter)
    def layer_parser(self,input):
        input=input.replace("MLPLayer_Size={","")
        input=input.replace("}","")
        pattern = r"(\d+),\((\d+),\"(\w+)\"\),\((\d+),\"(\w+)\"\)"
        pattern = r'\d+|\(\d+,\"\w+\"\)'
        matches = re.findall(pattern, input)
        print(matches)
        layers = []
        for match in matches:
            if '(' in match:
                size, activation = re.findall(r'\d+', match)[0], re.findall(r'\"(\w+)\"', match)[0]
                layers.append((int(size), activation))
            else:
                layers.append((int(match), None))
        return layers
    def is_operand(self, item):
        if item in self.non_operands:
            return False
        else:
            return True

    def generate_code(self, post_order_array):
        for item in post_order_array:
            if not self.is_operand(item["label"]):
                self.generate_program(item["label"])
            else:
                self.operand_stack.append(item["label"])
        return self.import_str+self.code
    def generate_program(self,rulename):
        if rulename=='data':
            self.generate_code_data()
        elif rulename=='poison_statement':
            self.generate_code_poison_statement()
        elif rulename=='data_statement':
            self.generate_code_data_statement()
        elif rulename=='model_statement':
            self.generate_code_model_statement()
        elif rulename=='plot_statement':
            self.generate_code_plot_statement()
        elif rulename=='metric':
            self.generate_code_metric()
        elif rulename=='json':
            self.generate_code_json()
        self.operand_stack.clear()
    def generate_code_data(self):
        action=self.operand_stack[0]
        dataset=self.operand_stack[2]
        if(action=='Load'):
            self.data_code=self.data_code+(f"# Loading dataset\ntransform = transforms.Compose([transforms.ToTensor()])\n"
                                           f"dataset = datasets.{dataset}(root='./data', train=True, transform=transform, download=True)\n\n"
                                           f"# Split dataset into train, validation, and test sets\n"
                                           f"total_size = len(dataset)\ntrain_size = int(train_ratio * total_size)\nval_size = int(val_ratio * total_size)\n"
                                           f"test_size = total_size - train_size - val_size\n"
                                           f"train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])\n")
        else:
            raise Exception("Aborting : Action on the dataset not supported")
    def generate_code_poison_statement(self):
        data=self.operand_stack[0]
        pattern = r'"(\d+|X)"->"(\d+|Y)"'
        matches = re.findall(pattern, data)
        poison_code=(f"def poison_dataset(dataset, poison_ratio):\n"
                     f"\ttargets = np.array(dataset.dataset.targets)\n"
                     f"\tindices = dataset.indices\n\n")
        for item in matches:
            new_label=self.create_new_label(item[0])

            poison_code=poison_code+(f"\t{new_label} = [i for i in indices if targets[i] == {int(item[0]) if item[0].isdigit() else item[0]}]\n"
                                     f"\tnum_to_flip = int(len({new_label}) * poison_ratio)\n\n"
                                     f"\tflip_indices = np.random.choice({new_label}, num_to_flip, replace=False)\n"
                                     f"\tfor idx in flip_indices:\n"
                                     f"\t\tdataset.dataset.targets[idx] = {int(item[1]) if item[1].isdigit() else item[1]}\n\n")
        self.data_code=self.data_code+poison_code+"poison_dataset(train_dataset, poison_ratio)\n\n\n"



    def generate_code_data_statement(self):
        self.data_code+=(f"train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)\n"
                         f"val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=False)\n"
                         f"test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)\n\n")
        self.code = self.code + self.data_code
    def generate_code_model_statement(self):
        input=self.operand_stack[0]
        layers=self.layer_parser(input)
        base_code=(f"class MLP(nn.Module):\n"
                   f"\tdef __init__(self):\n"
                   f"\t\tsuper(MLP, self).__init__()\n")
        forward_code=(f"\tdef forward(self, x):\n"
                      f"\t\tx = x.view(x.size(0), -1)\n"
                      )
        print(layers)
        for i in range(0,len(layers)-1):
            if layers[i+1][1]==None or layers[i+1][1]=="softmax" :
                label=self.create_layer_label()
                base_code=base_code+f"\t\tself.{label} = nn.Linear({layers[i][0]}, {layers[i+1][0]})\n"
                forward_code=forward_code+f"\t\tx = self.{label}(x)\n"
            else:
                label=self.create_layer_label()
                base_code=base_code+f"\t\tself.{label} = nn.Linear({layers[i][0]}, {layers[i+1][0]})\n"
                forward_code=forward_code+f"\t\tx = torch.{layers[i+1][1]}(self.{label}(x))\n"
        last_label=self.create_layer_label()
        forward_code+=f"\n\t\treturn x\n\n"
        self.code+=base_code+forward_code
        self.code+=self.generate_train_loop_code()


    def generate_code_plot_statement(self):
        pass
    def generate_code_metric(self):
        metric=self.operand_stack[0]
        if metric=='val_acc':
            with open('./config/validation_plot.cg', 'r') as file:
                data = file.read()
                self.code += "\n\n"+data+"\n\n"
        elif metric=='confusion_matrix':
            with open('./config/confusion.cg', 'r') as file:
                data = file.read()
                self.code += "\n\n"+data+"\n\n"
        elif metric=='accuracy':
            with open('./config/accuracy.cg', 'r') as file:
                data = file.read()
                self.code += "\n\n"+data+"\n\n"





    def generate_code_json(self):
        hyperparameter_code=""
        if(self.operand_stack[0]=='use_json'):
            self.used_json=True
            with open('./config/hyper.json', 'r') as file:
                data = json.load(file)
            hyperparameter_code=(f"\n# Hyperparameters\n"
            f"train_ratio = {data["train_ratio"]}\n"
            f"val_ratio = {data["validation_ratio"]}\n"
            f"test_ratio = {1-(data["validation_ratio"]+data["train_ratio"]):.2f}\n"
            f"batch_size = {data["batch_size"]}\n"
            f"num_epochs = {data["EPOCHS"]}\n"
            f"learning_rate = {data["learning_rate"]}\n"
            f"poison_ratio = {data["poison_ratio"]}\n")
        else:
            hyperparameter_code=(f"\n# Hyperparameters\n"
            f"train_ratio = 0.7\n"
            f"val_ratio = 0.15\n"
            f"test_ratio = 0.15\n"
            f"batch_size = 64\n"
            f"num_epochs = 10\n"
            f"learning_rate = 0.001\n"
            f"poison_ratio = 0.2\n")
        self.data_code=hyperparameter_code+self.data_code

