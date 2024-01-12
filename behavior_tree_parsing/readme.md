# Behavior Tree to NuSMV Model Encoder

## Overview
This Python script is designed to encode Behavior Trees, which are defined in XML format, into corresponding NuSMV models. It analyzes the Behavior Tree, recognizing actions and their organizational patterns (sequences or selectors), and creates an equivalent NuSMV model.

## Features
- **XML Parsing**: Efficiently processes XML-based Behavior Trees.
- **Node Handling**: Accurately handles various node types, including Actions, Sequences, and Selectors.
- **NuSMV Model Creation**: Generates NuSMV models with proper variable definitions and state transitions.

## Requirements
- Python 3.x
- XML files of Behavior Trees for input.

## Installation
No additional installation is required beyond a standard Python environment.

## Usage
### Preparing the Behavior Tree XML File
1. Create an XML file representing your Behavior Tree.
2. Follow the structure outlined in the provided templates.

### Running the Script
- Execute the script, using the XML file as input.
- The script will parse the Behavior Tree and produce a NuSMV model.

## Input Format
- The Behavior Tree should be in XML format.
- The XML should have nested elements representing the tree's structure, including Actions, Sequences, and Selectors.

### Example
```xml
<root main_tree_to_execute="MainTree">
    <BehaviorTree ID="MainTree">
        <Sequence name="Root">
            <Action name="SomeAction"/>
        </Sequence>
    </BehaviorTree>
</root>
```

## Output Format
- The output is a NuSMV model file.
- It includes state variables for each action and the logic for transitions.

## Limitations
- The tool requires well-formed XML as input. 

