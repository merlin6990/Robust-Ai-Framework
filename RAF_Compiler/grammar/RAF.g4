grammar RAF;

start: data_statement model_statement (plot_statement)? ;

data_statement : data+ json (poison_statement)?;
data :action dataset;
dataset: 'MNIST'|'CIFAR';
json : 'use_json'|'use_default';
action : 'Load'|'Save';
model_statement: mlp;

mlp: 'MLP' 'Layer_Size={' size(',('size','activation')')+'}';
size : INTEGER;
activation : '"relu"' | '"sigmoid"' | '"softmax"';

plot_statement: 'plot' metric+;
metric: ('val_acc'|'confusion_matrix'|'accuracy'|'backdoor_stat');

poison_statement returns [datatype=str()]:
                  label_flip #label_function
                  |backdoor #backdoor_function;

label_flip: 'flip_poison' flip_statement;
flip_statement: ( label '->' label (','?))+;
backdoor: 'backdoor' ':=' '{' 'src_class' ':' src ',' 'target_class' ':' target  pattern+ '}';
pattern: ',' '(' x ',' y ','a ','b ')';
label:String;

src:String;
target:String;
x:INTEGER;
y:INTEGER;
a:INTEGER;
b:INTEGER;

WS: [ \t\r\n]+ -> skip;
INTEGER: [1-9] [0-9]*;
String: '"' (ESC | .)*? '"';
fragment ESC: '\\"' | '\\\\';