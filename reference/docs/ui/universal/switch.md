---
title: "Switch"
description: "A toggle control that switches between on and off states."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/switch.md"
scraped_at: "2026-07-15T09:01:36.772142"
---

---
title: Switch
description: A toggle control that switches between on and off states.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Switch

A toggle control that switches between on and off states.
Android, iOS, Web, Included in Expo Go

A controlled toggle. Pair [`value`](/versions/latest/sdk/ui/universal/switch.md#value) with [`onValueChange`](/versions/latest/sdk/ui/universal/switch.md#onvaluechange) to manage state from React.

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

### Basic switch

```tsx
import { useState } from 'react';
import { Host, Switch } from '@expo/ui';

export default function SwitchExample() {
  const [enabled, setEnabled] = useState(false);

  return (
    <Host matchContents>
      <Switch value={enabled} onValueChange={setEnabled} />
    </Host>
  );
}
```

### With label

When `label` is provided, the switch is rendered alongside its text in a labeled row.

```tsx
import { useState } from 'react';
import { Host, Switch } from '@expo/ui';

export default function LabeledSwitchExample() {
  const [notifications, setNotifications] = useState(true);

  return (
    <Host style={{ flex: 1 }}>
      <Switch label="Enable notifications" value={notifications} onValueChange={setNotifications} />
    </Host>
  );
}
```

## API

```tsx
import { Switch } from '@expo/ui';
```

## Component

### `Switch`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SwitchProps](#switchprops)\>

A toggle control that switches between on and off states.

Props for the [`Switch`](#switch) component, a toggle control.

SwitchProps

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the switch is disabled. Disabled switches do not respond to user interaction.

### `label`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Text label displayed alongside the switch.

### `modifiers`

Supported platforms: Android, iOS, Web.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`.

### `onValueChange`

Supported platforms: Android, iOS, Web.

Type: `(value: boolean) => void`

Called when the user toggles the switch.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `value`

Supported platforms: Android, iOS, Web.

Type: `boolean`

Whether the switch is on.
