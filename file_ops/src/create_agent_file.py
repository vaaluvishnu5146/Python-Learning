from dataclasses import dataclass, asdict
import json

@dataclass
class AgentInfo:
    name: str
    age: int

dict = {
    "name": 'Vishnu',
    "age": 30,
    "city": "Pollachi"
}

file = 'agent_configs.json'

try:
    with open(file, "r") as jsonFile:
        content = jsonFile.read()
        print("Content =>", content)
except FileNotFoundError as error:
    print("Error", f"File {file} is not found")

# with open("agent_config.json", "r") as agentInfo:
#     content = agentInfo.read()
