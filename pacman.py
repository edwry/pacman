#!/usr/bin/env python3

# Environment: https://gymnasium.farama.org/environments/atari/pacman/

# Learning points:
# * Observation and Reward function is clearly defined here (simplistic relative to practical or "real life" situations)

import gymnasium as gym

STEPS=10**3

def main():
  env = gym.make("ALE/Pacman-v5", render_mode="human")

  env.reset()
  for _ in range(STEPS):
    action = env.action_space.sample()  # agent policy that uses the observation and info
    observation, reward, terminated, truncated, info = env.step(action)
    if terminated or truncated:
      observation, info = env.reset()
  env.close()

if __name__=="__main__":
  main()
