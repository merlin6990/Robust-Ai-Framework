# Robust-Ai-Framework
## Problem Definition
Adversarial machine learning is the study
of attacks on machine learning algorithms and defenses against such attacks.
These attacks can take on many forms, such as data poisoning attacks, back-
door attacks, model stealing, etc. The main problem is that there does not exist
a singular framework in which you can test, analyze, and measure the impact of
various attacks and their respective defenses. As a result, many of these attacks can be considered vague as they might only work in specific configurations and
might not be applicable in many scenarios.
## Solution
To address this issue, we propose
RAF, aka Robust AI Framework, a DSL that specializes in the simulation, eval-
uation, and code generation of adversarial attacks and their defenses in a unified
way. Due to the variety of adversarial attacks and their respective defenses, we
would minimize the scope of our project to ensure it becomes apparent that not
only does our solution work, but it can also be generalized to cover all attacks
available in real scenarios.
## Project Overview
The overview of the RAF compiler can be found in Figure 2, where our compiler
takes *.raf as an input file and generates the Python code for the attack and/or
defense. For the scope of this project, we will implement two scenarios: data
poisoning attack and DP-SGD as a defense mechanism.
