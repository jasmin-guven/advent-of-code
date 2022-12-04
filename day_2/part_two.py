import pandas as pd

input = pd.read_csv("input.txt", sep="\s+", header=None, names=["opponent", "expected_response"])

convert_values = lambda df, column, old, new: df[column].replace(old, new)
input["opponent"] = convert_values(input, "opponent", "A", "rock")
input["opponent"] = convert_values(input, "opponent", "B", "paper")
input["opponent"] = convert_values(input, "opponent", "C", "scissors")
# input["response_score"] = input["expected_response"]
# input["response_score"] = convert_values(input, "response_score", "X", 1)
# input["response_score"] = convert_values(input, "response_score", "Y", 2)
# input["response_score"] = convert_values(input, "response_score", "Z", 3)

opponent = input["opponent"].to_list()
expected_response = input["expected_response"].to_list()
expected_outcomes = []
for i in range(len(opponent)):
    if expected_response[i] == "X":
        expected_outcomes.append("lose")
    elif expected_response[i] == "Y":
        expected_outcomes.append("draw")
    elif expected_response[i] == "Z":
        expected_outcomes.append("win")

input["expected"] = expected_outcomes

response = []
for i in range(len(opponent)):
    if expected_outcomes[i] == "draw":
        response.append(opponent[i])
    elif expected_outcomes[i] == "lose" and opponent[i] == "rock":
        response.append("scissors")
    elif expected_outcomes[i] == "lose" and opponent[i] == "paper":
        response.append("rock")
    elif expected_outcomes[i] == "lose" and opponent[i] == "scissors":
        response.append("paper")
    elif expected_outcomes[i] == "win" and opponent[i] == "rock":
        response.append("paper")
    elif expected_outcomes[i] == "win" and opponent[i] == "paper":
        response.append("scissors")
    elif expected_outcomes[i] == "win" and opponent[i] == "scissors":
        response.append("rock")

df = input.copy()
df["expected_response"] = response
outcomes = df.rename(columns={"expected_response": "response"})
outcomes["response_score"] = outcomes["response"]
outcomes["response_score"] = convert_values(outcomes, "response_score", "rock", 1)
outcomes["response_score"] = convert_values(outcomes, "response_score", "paper", 2)
outcomes["response_score"] = convert_values(outcomes, "response_score", "scissors", 3)
outcomes["outcome_score"] = outcomes["expected"]
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "lose", 0)
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "draw", 3)
outcomes["outcome_score"] = convert_values(outcomes, "outcome_score", "win", 6)

outcomes["score"] = outcomes["response_score"] + outcomes["outcome_score"]
total_score = outcomes["score"].sum()
print(outcomes.head())

print(f"Total score: {total_score}")
