# Expo Agent Skill

A comprehensive AI agent skill that enforces reading offline Expo and React Native documentation before writing code. This skill prevents the AI from hallucinating APIs or using outdated React Native syntax by enforcing a strict "doc-first loop" pattern.

## Features

- **Navigation-First Protocol**: Prevents the agent from parsing entire directories and blowing up token limits.
- **Incremental Reading**: Directs the agent to map the domain, pinpoint the module in `AGENTS.md`, and surgically read the specific `.md` file for the API.
- **Offline Documentation**: Comes bundled with the `reference/docs/` folder containing offline Markdown documentation for Expo v56, parsed from official Expo docs.
- **Automatic Upgrades**: Bundled with a suite of Python scripts (`scripts/`) to re-crawl or update the offline documentation when new Expo SDK versions are released.

## Installation

You can install this skill into your project's `.agents/skills/` directory.

```bash
git clone https://github.com/your-username/expo-agent-skill.git .agents/skills/expo-agent
```

## Usage

Once installed, your AI agent will automatically detect the `expo-agent` skill if it supports model-invoked skills (the `disable-model-invocation` flag is not set). 

Whenever you ask the agent to:
- Build an Expo app
- Add a new Expo module
- Debug React Native code

The agent will automatically trigger the `doc-first` loop defined in `SKILL.md` to ground its code in the offline reference documentation.

## Updating the Offline Docs (Optional)

If you need to update the offline docs to a newer Expo SDK version, you can run the crawler scripts provided in `scripts/`:

```bash
cd scripts/
# Crawl the entire Expo SDK (it will automatically categorize and save to reference/docs)
python3 crawl_all_sdk.py

# Re-generate the AGENTS.md navigation indexes
python3 generate_agents_md.py
```

## License

MIT
