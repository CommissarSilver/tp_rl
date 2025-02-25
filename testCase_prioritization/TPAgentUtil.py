#
from stable_baselines.common import make_vec_env
from stable_baselines.common.vec_env import DummyVecEnv
import numpy as np

from PairWiseEnv import CIPairWiseEnv

# !!! PAY HEED BROTHER: The documentation for these algorithms can be found at: https://stable-baselines.readthedocs.io/en/master/index.html
# !!! For each algorithm, the hyperparameters and their default values are outlined


class TPAgentUtil:
    # supported_algo = ['DQN', 'PPO2', "A2C", "ACER", "ACKTR", "HER", "PPO1", "TRPO"]
    supported_algo = [
        "DQN",
        "PPO2",
        "A2C",
        "ACKTR",
        "DDPG",
        "ACER",
        "GAIL",
        "HER",
        "PPO1",
        "SAC",
        "TD3",
        "TRPO",
    ]

    def create_model(algo, env):
        assert TPAgentUtil.supported_algo.count(algo.upper()) == 1, (
            "The algorithms  is not supported for" " pairwise formalization"
        )
        if algo.upper() == "DQN":
            # ======================= HYPER-PARAMS =======================
            # gamma: discount factor
            # learning_rate: learning rate
            # exploration_fraction: fraction of entire training period over which the exploration rate is annealed
            # exploration_final_eps: final value of random action probability
            # exploration_initial_eps: initial value of random action probability
            # train_freq: (int) update the model every train_freq steps. set to None to disable printing
            # learning_starts: (int) how many steps of the model to collect transitions for before learning starts
            # target_network_update_freq: (int) update the target network every target_network_update_freq steps.
            # prioritized_replay_alpha: alpha parameter for prioritized replay buffer. It determines how much prioritization is used, with alpha=0 corresponding to the uniform case.
            # prioritized_replay_beta0: initial value of beta for prioritized replay buffer
            # prioritized_replay_beta_iters: (int) number of iterations over which beta will be annealed from initial value to 1.0. If set to None equals to max_timesteps.
            # prioritized_replay_eps: epsilon to add to the TD errors when updating priorities.
            # ======================= HYPER-PARAMS =======================
            from stable_baselines import DQN
            from stable_baselines.deepq.policies import MlpPolicy

            model = DQN(
                MlpPolicy,
                env,
                gamma=0.90,
                learning_rate=0.0005,
                buffer_size=10000,
                exploration_fraction=1,
                exploration_final_eps=0.02,
                exploration_initial_eps=1.0,
                train_freq=1,
                batch_size=32,
                double_q=True,
                learning_starts=1000,
                target_network_update_freq=500,
                prioritized_replay=False,
                prioritized_replay_alpha=0.6,
                prioritized_replay_beta0=0.4,
                prioritized_replay_beta_iters=None,
                prioritized_replay_eps=1e-06,
                param_noise=False,
                n_cpu_tf_sess=None,
                verbose=0,
                tensorboard_log=None,
                _init_setup_model=True,
                policy_kwargs=None,
                full_tensorboard_log=False,
                seed=None,
            )
        elif algo.upper() == "PPO2":
            # ======================= HYPER-PARAMS =======================
            # gamma: discount factor
            # learning_rate: learning rate
            # n_steps: (int) The number of steps to run for each environment per update (i.e. batch size is n_steps * n_env where n_env is number of environment copies running in parallel)
            # ent_coef: (float) Entropy coefficient for the loss calculation
            # vf_coef: (float) Value function coefficient for the loss calculation
            # max_grad_norm: (float) The maximum value for the gradient clipping
            # noptepochs: (int) Number of epoch when optimizing the surrogate
            # ======================= HYPER-PARAMS =======================
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.ppo2 import PPO2

            env = DummyVecEnv([lambda: env])
            model = PPO2(MlpPolicy, env, verbose=0)
        elif algo.upper() == "TD3":
            # ======================= HYPER-PARAMS =======================
            # gamma: discount factor
            # learning_rate: learning rate
            # tau: (float) the soft update coefficient (“polyak update” of the target networks, between 0 and 1)
            # policy_delay: (int) Policy and target networks will only be updated once every policy_delay steps per training steps. The Q values will be updated policy_delay more often (update every training step).
            # target_policy_noise: (float) Standard deviation of Gaussian noise added to target policy (smoothing noise)
            # target_noise_clip: (float) Limit for absolute value of target policy smoothing noise.
            # train_freq: (int) Update the model every train_freq steps.
            # gradient_steps: (int) How many gradient update after each step
            # random_exploration: (float) Probability of taking a random action (as in an epsilon-greedy strategy) This is not needed for TD3 normally but can help exploring when using HER + TD3. This hack was present in the original OpenAI Baselines repo (DDPG + HER)
            # ======================= HYPER-PARAMS =======================
            from stable_baselines import TD3
            from stable_baselines.td3.policies import MlpPolicy

            env = DummyVecEnv([lambda: env])
            model = TD3(MlpPolicy, env, verbose=0)
        elif algo.upper() == "A2C":
            # ======================= HYPER-PARAMS =======================
            # gamma: discount factor
            # learning_rate: learning rate
            # vf_coef: (float) Value function coefficient for the loss calculation
            # ent_coef: (float) Entropy coefficient for the loss calculation
            # max_grad_norm: (float) The maximum value for the gradient clipping
            # alpha: (float) RMSProp decay parameter (default: 0.99)
            # momentum: (float) RMSProp momentum parameter (default: 0.0)
            # epsilon: (float) RMSProp epsilon (stabilizes square root computation in denominator of RMSProp update) (default: 1e-5)
            # lr_schedule: (str) The type of scheduler for the learning rate update (‘linear’, ‘constant’, ‘double_linear_con’, ‘middle_drop’ or ‘double_middle_drop’)
            # ======================= HYPER-PARAMS =======================
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.a2c import A2C

            env = DummyVecEnv([lambda: env])
            model = A2C(
                MlpPolicy,
                env,
                gamma=0.90,
                learning_rate=0.0005,
                n_cpu_tf_sess=None,
                verbose=0,
                tensorboard_log=None,
                _init_setup_model=True,
                policy_kwargs=None,
                full_tensorboard_log=False,
                seed=None,
            )
        elif algo.upper() == "ACER":
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.acer import ACER

            env = DummyVecEnv([lambda: env])
            model = ACER(MlpPolicy, env, replay_ratio=0, verbose=0)
            # model = ACER(MlpPolicy, env,  verbose=1)
        elif algo.upper() == "ACKTR":
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.acktr import ACKTR

            env = DummyVecEnv([lambda: env])
            model = ACKTR(MlpPolicy, env, verbose=0)
        elif algo.upper() == "GAIL":
            assert False, "GAIL is not implemented"
            from stable_baselines.common.policies import MlpPolicy
            import stable_baselines.gail
        elif algo.upper() == "HER":
            assert False, "HER is not implemented"
            import stable_baselines.her

            pass
        elif algo.upper() == "PPO1":
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.ppo1 import PPO1

            env = DummyVecEnv([lambda: env])
            model = PPO1(MlpPolicy, env, verbose=0)

        elif algo.upper() == "TRPO":
            from stable_baselines.common.policies import MlpPolicy
            from stable_baselines.trpo_mpi import TRPO

            env = DummyVecEnv([lambda: env])
            model = TRPO(MlpPolicy, env, verbose=0)
        elif algo.upper() == "DDPG":
            from stable_baselines.ddpg.policies import MlpPolicy
            from stable_baselines import DDPG

            env = DummyVecEnv([lambda: env])
            model = DDPG(MlpPolicy, env, verbose=0)
        elif algo.upper() == "SAC":
            from stable_baselines.sac.policies import MlpPolicy
            from stable_baselines import SAC

            env = DummyVecEnv([lambda: env])
            model = SAC(MlpPolicy, env, verbose=0)

        return model

    def load_model(algo, env, path):
        if algo.upper() == "DQN":
            from stable_baselines.deepq import DQN

            model = DQN.load(path)
            model.set_env(env)
        elif algo.upper() == "PPO2":
            from stable_baselines.ppo2 import PPO2

            model = PPO2.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "A2C":
            from stable_baselines.a2c import A2C

            model = A2C.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "ACER":
            from stable_baselines.acer import ACER

            model = ACER.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "ACKTR":
            from stable_baselines.acktr import ACKTR

            model = ACKTR.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "GAIL":
            import stable_baselines.gail
        elif algo.upper() == "HER":
            import stable_baselines.her

            pass
        elif algo.upper() == "PPO1":
            from stable_baselines.ppo1 import PPO1

            model = PPO1.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "TRPO":
            from stable_baselines.trpo_mpi import TRPO

            model = TRPO.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "DDPG":
            from stable_baselines.ddpg.policies import MlpPolicy
            from stable_baselines import DDPG

            model = DDPG.load(path)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "TD3":
            from stable_baselines import TD3
            from stable_baselines.td3.policies import MlpPolicy

            model = TD3(MlpPolicy, env, verbose=0)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        elif algo.upper() == "SAC":
            from stable_baselines.sac.policies import MlpPolicy
            from stable_baselines import SAC

            model = SAC(MlpPolicy, env, verbose=0)
            env = DummyVecEnv([lambda: env])
            model.set_env(env)
        else:
            return None
        return model

    def test_agent(env: CIPairWiseEnv, model_path: str, algo, mode):
        agent_actions = []
        print("Evaluation of an agent from " + model_path)
        model = TPAgentUtil.load_model(path=model_path, algo=algo, env=env)
        if model:
            if mode.upper() == "PAIRWISE" and algo.upper() != "DQN":
                env = model.get_env()
                obs = env.reset()
                done = False
                while True:
                    action, _states = model.predict(obs, deterministic=True)
                    # print(action)
                    obs, rewards, done, info = env.step(action)
                    if done:
                        break
                return env.get_attr("sorted_test_cases_vector")[0]
            elif mode.upper() == "PAIRWISE" and algo.upper() == "DQN":
                env = model.get_env()
                obs = env.reset()
                done = False
                while True:
                    action, _states = model.predict(obs, deterministic=True)
                    obs, rewards, done, info = env.step(action)
                    if done:
                        break
                return env.sorted_test_cases_vector
            elif mode.upper() == "POINTWISE":
                if model:
                    test_cases = env.cycle_logs.test_cases
                    if algo.upper() != "DQN":
                        env = DummyVecEnv([lambda: env])
                    model.set_env(env)
                    obs = env.reset()
                    done = False
                    index = 0
                    test_cases_vector_prob = []
                    for index in range(0, len(test_cases)):
                        action, _states = model.predict(obs, deterministic=True)
                        # print(action)
                        obs, rewards, done, info = env.step(action)
                        test_cases_vector_prob.append({"index": index, "prob": action})
                        if done:
                            assert len(test_cases) == index + 1, (
                                "Evaluation is finished without iterating all "
                                "test cases "
                            )
                            break
                    test_cases_vector_prob = sorted(
                        test_cases_vector_prob, key=lambda x: x["prob"], reverse=False
                    )  ## the lower the rank, te higher the priority
                    sorted_test_cases = []
                    for test_case in test_cases_vector_prob:
                        sorted_test_cases.append(test_cases[test_case["index"]])
                return sorted_test_cases
                pass
            elif mode.upper() == "LISTWISE":
                if model:
                    test_cases = env.cycle_logs.test_cases
                    if algo.upper() != "DQN":
                        env = DummyVecEnv([lambda: env])
                    model.set_env(env)
                    obs = env.reset()
                    done = False
                i = 0
                while True and i < 1000000:
                    i = i + 1
                    action, _states = model.predict(obs, deterministic=False)
                    # print(action)
                    # print(len(agent_actions))
                    if agent_actions.count(action) == 0 and action < len(test_cases):
                        if isinstance(action, list) or isinstance(action, np.ndarray):
                            agent_actions.append(action[0])
                        else:
                            agent_actions.append(action)
                        # print(len(agent_actions))
                    obs, rewards, done, info = env.step(action)
                    if done:
                        break
                sorted_test_cases = []

                for index in agent_actions:
                    sorted_test_cases.append(test_cases[index])
                if i >= 1000000:
                    sorted_test_cases = test_cases
                return sorted_test_cases
            elif mode.upper() == "LISTWISE2":
                if model:
                    env = model.get_env()
                    obs = env.reset()
                    action, _states = model.predict(obs, deterministic=True)
                    env.step(action)
                    if algo.upper() != "DQN":
                        return env.get_attr("sorted_test_cases")[0]
                    else:
                        return env.sorted_test_cases
