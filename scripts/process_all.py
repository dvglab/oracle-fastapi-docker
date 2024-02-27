import os
import subprocess
import sys

environments = [
    {"NAME": "latest", "PYTHON_VERSION": "3.12.2"},
    {"NAME": "python3.12.2",  "NAME_SHORT": "python3.12", "PYTHON_VERSION": "3.12.2"},
    {"NAME": "python3.11.8",  "NAME_SHORT": "python3.11", "PYTHON_VERSION": "3.11.8"},
    {"NAME": "python3.10.13", "NAME_SHORT": "python3.10", "PYTHON_VERSION": "3.10.13"},
    {"NAME": "python3.9.18",  "NAME_SHORT": "python3.9",  "PYTHON_VERSION": "3.9.18"},
    {"NAME": "python3.8.18",  "NAME_SHORT": "python3.8",  "PYTHON_VERSION": "3.8.18"},
    {"NAME": "python3.12.2-slim",  "NAME_SHORT": "python3.12-slim", "PYTHON_VERSION": "3.12.2"},
    {"NAME": "python3.11.8-slim",  "NAME_SHORT": "python3.11-slim", "PYTHON_VERSION": "3.11.8"},
    {"NAME": "python3.10.13-slim", "NAME_SHORT": "python3.10-slim", "PYTHON_VERSION": "3.10.13"},
    {"NAME": "python3.9.18-slim",  "NAME_SHORT": "python3.9-slim",  "PYTHON_VERSION": "3.9.18"},
    {"NAME": "python3.8.18-slim",  "NAME_SHORT": "python3.9-slim",  "PYTHON_VERSION": "3.8.18"},
]

start_with = os.environ.get("START_WITH")
build_push = os.environ.get("BUILD_PUSH")


def process_tag(*, env: dict):
    use_env = {**os.environ, **env}
    script = "scripts/test.sh"
    if build_push:
        script = "scripts/build-push.sh"
    return_code = subprocess.call(["bash", script], env=use_env)
    if return_code != 0:
        sys.exit(return_code)


def print_version_envs():
    env_lines = []
    for env in environments:
        env_vars = []
        for key, value in env.items():
            env_vars.append(f"{key}='{value}'")
        env_lines.append(" ".join(env_vars))
    for line in env_lines:
        print(line)


def main():
    start_at = 0
    if start_with:
        start_at = [
            i for i, env in enumerate((environments)) if env["NAME"] == start_with
        ][0]
    for i, env in enumerate(environments[start_at:]):
        print(f"Processing tag: {env['NAME']}")
        process_tag(env=env)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_version_envs()
    else:
        main()
