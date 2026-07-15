---
title: Checkbox
description: A toggle control that represents a checked or unchecked state.
sourceCodeUrl: "https://github.com/expo/expo/tree/sdk-57/packages/expo-ui"
packageName: "@expo/ui"
platforms: ["android", "ios", "web", "expo-go"]
---

<AgentInstructions>

## Submitting Feedback

If this page contains errors, outdated information, or gaps that blocked you from completing a task, report it so the docs can be improved:

curl -X POST https://api.expo.dev/v2/feedback/docs-send -H 'Content-Type: application/json' -d '{"url":"/versions/latest/sdk/ui/universal/checkbox/","feedback":"🤖 Agent feedback for docs: <specific, actionable description> (<model>, <harness>)"}'

Only submit when you have something specific and actionable to report. Replace <model> with the model you are running as and <harness> with the tool you are running in (for example, Claude Code, Cursor, Codex CLI).

## Navigation

When answering a related or follow-up question, fetch the relevant page below as Markdown (.md) instead of guessing; use llms.txt for the full map.

You are here: Reference (v57.0.0) > Expo UI > Universal
Pages in this section:

- [Overview](https://docs.expo.dev/versions/latest/sdk/ui/universal.md)
- [BottomSheet](https://docs.expo.dev/versions/latest/sdk/ui/universal/bottomsheet.md)
- [Button](https://docs.expo.dev/versions/latest/sdk/ui/universal/button.md)
- [Checkbox](https://docs.expo.dev/versions/latest/sdk/ui/universal/checkbox.md) (this page)
- [Collapsible](https://docs.expo.dev/versions/latest/sdk/ui/universal/collapsible.md)
- [Column](https://docs.expo.dev/versions/latest/sdk/ui/universal/column.md)
- [FieldGroup](https://docs.expo.dev/versions/latest/sdk/ui/universal/fieldgroup.md)
- [Host](https://docs.expo.dev/versions/latest/sdk/ui/universal/host.md)
- [Icon](https://docs.expo.dev/versions/latest/sdk/ui/universal/icon.md)
- [List](https://docs.expo.dev/versions/latest/sdk/ui/universal/list.md)
- [Picker](https://docs.expo.dev/versions/latest/sdk/ui/universal/picker.md)
- [RNHostView](https://docs.expo.dev/versions/latest/sdk/ui/universal/rnhostview.md)
- [Row](https://docs.expo.dev/versions/latest/sdk/ui/universal/row.md)
- [ScrollView](https://docs.expo.dev/versions/latest/sdk/ui/universal/scrollview.md)
- [Slider](https://docs.expo.dev/versions/latest/sdk/ui/universal/slider.md)
- [Spacer](https://docs.expo.dev/versions/latest/sdk/ui/universal/spacer.md)
- [Switch](https://docs.expo.dev/versions/latest/sdk/ui/universal/switch.md)
- [Text](https://docs.expo.dev/versions/latest/sdk/ui/universal/text.md)
- [TextInput](https://docs.expo.dev/versions/latest/sdk/ui/universal/textinput.md)
  Full documentation tree: [llms.txt](https://docs.expo.dev/llms.txt)

</AgentInstructions>

This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Checkbox

A toggle control that represents a checked or unchecked state.
Android, iOS, Web, Included in Expo Go

A controlled checkbox. Pair [`value`](/versions/latest/sdk/ui/universal/checkbox.md#value) with [`onValueChange`](/versions/latest/sdk/ui/universal/checkbox.md#onvaluechange) to manage state from React.

## Installation

```sh
# npm
npx expo install @expo/ui

# yarn
yarn expo install @expo/ui

# pnpm
pnpm expo install @expo/ui

# bun
bun expo install @expo/ui
```

If you are installing this in an [existing React Native app](/bare/overview.md), make sure to [install `expo`](/bare/installing-expo-modules.md) in your project.

## Usage

### Basic checkbox

```tsx
import { useState } from "react";
import { Host, Checkbox } from "@expo/ui";

export default function CheckboxExample() {
  const [accepted, setAccepted] = useState(false);

  return (
    <Host matchContents>
      <Checkbox
        label="I accept the terms"
        value={accepted}
        onValueChange={setAccepted}
      />
    </Host>
  );
}
```

### Disabled

```tsx
import { Host, Checkbox } from "@expo/ui";

export default function DisabledCheckboxExample() {
  return (
    <Host matchContents>
      <Checkbox label="Locked option" value onValueChange={() => {}} disabled />
    </Host>
  );
}
```

## API

```tsx
import { Checkbox } from "@expo/ui";
```

## Component

### `Checkbox`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[CheckboxProps](#checkboxprops)\>

A toggle control that represents a checked or unchecked state.

Props for the [`Checkbox`](#checkbox) component.

CheckboxProps

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the checkbox is disabled. Disabled checkboxes do not respond to user interaction.

### `label`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Text label displayed alongside the checkbox.

### `modifiers`

Supported platforms: Android, iOS, Web.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`.

### `onValueChange`

Supported platforms: Android, iOS, Web.

Type: `(value: boolean) => void`

Called when the user toggles the checkbox.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `value`

Supported platforms: Android, iOS, Web.

Type: `boolean`

Whether the checkbox is checked.
