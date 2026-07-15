---
name: expo-agent
description: Guides the agent to build React Native and Expo applications using the local offline docs/ directory. Enforces reading relevant documents incrementally before writing code.
version: 1.0.0
---

## Navigation-First Protocol

You must use the **doc-first** loop whenever you are asked to write, refactor, or debug React Native and Expo code. The goal is to enforce reading relevant local documentation before writing code to prevent guessing APIs and syntax.

> [!IMPORTANT]
> Do NOT read the entire `docs/` directory. Doing so will blow up the token budget. Instead, traverse the documentation incrementally using the steps below.

### The Doc-First Loop

1. **Category Mapping**: Consult [AGENTS.md](./reference/docs/AGENTS.md) to locate which functional folder contains the module you need (e.g., `media/`, `sensors/`, `ui/`, `router/`).
2. **Module Pinpointing**: Open [AGENTS.md](./reference/docs) (e.g., [ui/AGENTS.md](./reference/docs/ui/AGENTS.md)) to identify the exact markdown file representing the module you are building with (e.g., `audio.md`, `camera.md`, `button.md`).
3. **Targeted Reading**: Open the specific file using `view_file` (e.g., [media/audio.md](./reference/docs/media/audio.md)) and read only the sections relevant to your implementation (e.g., methods, props, code examples).
4. **Grounded Coding**: Write or modify your Expo code based strictly on the API definitions and examples found in the documentation. Do not invent APIs or use outdated versions.

### Category Reference

- **`data-storage/`**: Local database, persistent key-value storage (AsyncStorage, SQLite, SecureStore).
- **`hardware/`**: Device-specific metadata and system properties (Battery, Network, Cellular, Haptics).
- **`media/`**: Audio, video, images, camera captures (Audio, Video, Camera, ImagePicker).
- **`router/`**: Expo Router routing, links, stack layouts, native tabs navigation.
- **`sensors/`**: Device motions and environmental inputs (Accelerometer, Gyroscope, Location).
- **`services/`**: System interfaces (Auth, Contacts, Notifications, Speech, calendar).
- **`system/`**: App lifecycle, filesystem access, updates management (Filesystem, Updates, TaskManager).
- **`ui/`**: All UI components. Includes specialized subfolders:
  - **`jetpack-compose/`**: Jetpack Compose modules.
  - **`swift-ui/`**: iOS SwiftUI modules.
  - **`universal/`**: Cross-platform UI modules.
  - **`drop-in-replacements/`**: Core replacements.

### Completion Criteria

Before you finish writing any Expo code:
- [ ] You have verified that the code uses APIs matching the offline docs exactly.
- [ ] You have checked that no custom wrappers or deprecated methods are used.
- [ ] In your response, explicitly reference which file under `reference/docs/` was consulted to guide your solution.
