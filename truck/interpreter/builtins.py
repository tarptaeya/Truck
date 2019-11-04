import os
import sys

def update_env(env):
    env.update("sys", sys)
    env.update("str", str)
