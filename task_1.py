from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END


class User(TypedDict):

    uName : str
    uEmail : str
    uPhoneNo : int
    response : str


def userData(state : User) -> dict :
    greeting = f"heyy,{state['uName']} ! , your personal details are {state['uEmail']}, {state ['uPhoneNo']} !"
    return {"response":greeting}


GraphBuilder = StateGraph(User)
GraphBuilder.add_node("Message", userData)

GraphBuilder.add_edge(START, "Message")
GraphBuilder.add_edge("Message",END)

graph = GraphBuilder.compile()


initial_state = {"uName": "Dhruvik",
                  "uEmail": "Dhruvikgmail.com", 
                  "uPhoneNo": 3309049490,
                    "response": " "}
final_state = graph.invoke(initial_state)

print(final_state)