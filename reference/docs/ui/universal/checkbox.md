---
title: "Checkbox"
description: "A toggle control that represents a checked or unchecked state."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/checkbox.md"
scraped_at: "2026-07-15T09:01:40.340533"
---

---
title: Checkbox
description: A toggle control that represents a checked or unchecked state.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



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
import { useState } from 'react';
import { Host, Checkbox } from '@expo/ui';

export default function CheckboxExample() {
  const [accepted, setAccepted] = useState(false);

  return (
    <Host matchContents>
      <Checkbox label="I accept the terms" value={accepted} onValueChange={setAccepted} />
    </Host>
  );
}
```

### Disabled

```tsx
import { Host, Checkbox } from '@expo/ui';

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
import { Checkbox } from '@expo/ui';
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
