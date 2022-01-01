import this
import TPDRL
import TPAgentUtil

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


# The problem with this is that it is returning everything as a method. I don't think it is possible to change a functions variables.


class Member:
    """[summary]

    Args:
        TPAgentUtil ([type]): [description]
    """

    def __init__(self, algo, env) -> None:
        super().__init__()
        agent_model = TPAgentUtil.TPAgentUtil.create_model(algo=algo, env=env)
        # !!! Hyperparameter as input to the algorithm
        self.model = agent_model  # this line is useless

    def mutate(self):
        pass

    def crossover(self):
        pass

    def get_agent_params(self):
        agent_params = self.model.get_parameters()
        return agent_params


class Population:
    def __init__(
        self, population_size: int, population_algo: str, population_mode: str
    ) -> None:
        pass

def test():
    def another_test()