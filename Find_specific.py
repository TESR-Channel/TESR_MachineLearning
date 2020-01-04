# Find S Algorithm from Play Tennis
                    #      Sky    Temp   Humid    Wind    Water  Forcast
input_table_dataset = [
                        ["Sunny","Warm","Normal","Strong","Warm","Same"],
                        ["Sunny","Warm", "High" ,"Strong","Warm","Same"],
                        ["Rainy","Cold", "High" ,"Strong","Warm","Change"],
                        ["Sunny","Warm", "High", "Strong","Cool","Change"]
                            ]
                      # Play
output_table_dataset = ["Yes",
                        "Yes",
                        "No",
                        "Yes"]

def expand(input_dataset,S):
    for i in range(0,len(S)):
        if input_dataset[i] != S[i] and S[i] == "":
            S[i] = input_dataset[i]
        elif input_dataset[i] != S[i] and S[i] != "":
            S[i] = "?"
    return S

def find_S(input_dataset,output_dataset):
    S = [""] * len(input_dataset[0])
    for i in range(0,len(input_dataset)):
        if output_dataset[i] == "Yes":
            S = expand(input_dataset[i],S)
    return S

print(find_S(input_table_dataset,output_table_dataset))