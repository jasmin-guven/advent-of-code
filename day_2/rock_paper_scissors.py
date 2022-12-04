import pandas as pd

input = pd.read_csv("input.txt", sep="\s+", header=None, names=["opponent", "response"])

convert_values = lambda df, column, old, new: df[column].replace(old, new)
input["opponent"] = convert_values(input, "opponent", "A", "X")
input["opponent"] = convert_values(input, "opponent", "B", "Y")
input["opponent"] = convert_values(input, "opponent", "C", "Z")
input["response_score"] = input["response"]
input["response_score"] = convert_values(input, "response_score", "X", 1)
input["response_score"] = convert_values(input, "response_score", "Y", 2)
input["response_score"] = convert_values(input, "response_score", "Z", 3)

opponent = input["opponent"].to_list()
response = input["response"].to_list()
response_scores = input["response_score"].to_list()
# X > Z, Z > Y, Y > X 
round_outcomes = []
for i in range(len(opponent)):
    if opponent[i] == response[i]:
        round_outcomes.append("draw")
    elif (opponent[i] == "X" and response[i] == "Z") or \
         (opponent[i] == "Y" and response[i] == "X") or \
         (opponent[i] == "Z" and response[i] == "Y"):
        round_outcomes.append("lose")
    elif (opponent[i] == "Z" and response[i] == "X") or \
         (opponent[i] == "X" and response[i] == "Y") or \
         (opponent[i] == "Y" and response[i] == "Z"):
        round_outcomes.append("win")
outcomes = input.copy()
outcomes["outcome"] = round_outcomes
outcomes["outcome_score"] = outcomes["outcome"]
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "win", 6)
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "draw", 3)
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "lose", 0)

outcomes["scores"] = outcomes["response_score"] + outcomes["outcome_score"]
total_score = outcomes["scores"].sum()

print(f"Total score: {total_score}")
