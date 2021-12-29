import this
# !!! OK BROTHER. HERE'S HOW IT SHOULD GO:
#   1 - TPDRL.py -> experiment function (line 50):
#           This function creates the environment and the agent's model.
#           If you want to create your population, !!! THIS IS NOT THE PLACE !!!.
#           This is the higher level function where each agent gets trained.
#           So for you PBT to work, you need to create agents that inherit this function or call it in another function with the agent.
#   2 - TPAgentUtil.py -> create_model function (line 18):
#           This is where you need to think about going about your PBT fuckery.
#           Agents' models and policies plus their hyperparameters are created and initilized here.
#           Your PBT thingie should initialize the hyperparams and new models of the population here.
#   3 - *** pbt.py ***
#           stable-baselines has a function that allows modifying and accessing each model's parameters.
#           we need to access model parameters for copying the weights. The hyperparams are going to be another story.
# !!! The documetation says MODEL PARAMETERS. I don't know if it means weights or not. If not, then we just have to save and load models.
