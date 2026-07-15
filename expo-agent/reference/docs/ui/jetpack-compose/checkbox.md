---
title: "Checkbox"
description: "A Jetpack Compose Checkbox component for selection controls."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/checkbox.md"
scraped_at: "2026-07-15T09:00:45.421602"
---

---
title: Checkbox
description: A Jetpack Compose Checkbox component for selection controls.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Checkbox

A Jetpack Compose Checkbox component for selection controls.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Checkbox`](/versions/latest/sdk/ui/universal/checkbox.md) — it renders the appropriate native component per platform.

Expo UI Checkbox matches the official Jetpack Compose [Checkbox](https://developer.android.com/develop/ui/compose/components/checkbox) API.

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
import { Host, Checkbox } from '@expo/ui/jetpack-compose';

export default function CheckboxExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <Checkbox value={checked} onCheckedChange={setChecked} />
    </Host>
  );
}
```

### Custom colors

```tsx
import { useState } from 'react';
import { Host, Checkbox } from '@expo/ui/jetpack-compose';

export default function CustomColorsExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <Checkbox
        value={checked}
        onCheckedChange={setChecked}
        colors={{
          checkedColor: '#6200EE',
          checkmarkColor: '#FFFFFF',
        }}
      />
    </Host>
  );
}
```

### Select all (TriStateCheckbox)

Use `TriStateCheckbox` for a parent checkbox that reflects the state of its children. It supports three states: `'on'`, `'off'`, and `'indeterminate'`.

Apply the `toggleable` modifier to each `Row` to make the entire row (checkbox + label) tappable with correct accessibility semantics. When using `toggleable` on the row, omit `onCheckedChange`/`onClick` from the checkbox itself to avoid double-handling.

```tsx
import { useState } from 'react';
import { Host, Checkbox, TriStateCheckbox, Row, Column, Text } from '@expo/ui/jetpack-compose';
import { toggleable } from '@expo/ui/jetpack-compose/modifiers';

export default function SelectAllExample() {
  const [child1, setChild1] = useState(false);
  const [child2, setChild2] = useState(false);
  const [child3, setChild3] = useState(false);

  const parentState =
    child1 && child2 && child3 ? 'on' : !child1 && !child2 && !child3 ? 'off' : 'indeterminate';

  return (
    <Host matchContents>
      <Column>
        <Row
          verticalAlignment="center"
          modifiers={[
            toggleable(
              parentState === 'on',
              () => {
                const newState = parentState !== 'on';
                setChild1(newState);
                setChild2(newState);
                setChild3(newState);
              },
              { role: 'checkbox' }
            ),
          ]}>
          <TriStateCheckbox state={parentState} />
          <Text>Select all</Text>
        </Row>
        <Row
          verticalAlignment="center"
          modifiers={[toggleable(child1, () => setChild1(!child1), { role: 'checkbox' })]}>
          <Checkbox value={child1} />
          <Text>Option 1</Text>
        </Row>
        <Row
          verticalAlignment="center"
          modifiers={[toggleable(child2, () => setChild2(!child2), { role: 'checkbox' })]}>
          <Checkbox value={child2} />
          <Text>Option 2</Text>
        </Row>
        <Row
          verticalAlignment="center"
          modifiers={[toggleable(child3, () => setChild3(!child3), { role: 'checkbox' })]}>
          <Checkbox value={child3} />
          <Text>Option 3</Text>
        </Row>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Checkbox, TriStateCheckbox } from '@expo/ui/jetpack-compose';
```

## Components

### `Checkbox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[CheckboxProps](#checkboxprops)\>

A checkbox component.

CheckboxProps

### `colors`

Supported platforms: Android.

Optional • Type: [CheckboxColors](/versions/v57.0.0/sdk/ui/jetpack-compose/checkbox.md#checkboxcolors)

Colors for checkbox core elements.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the checkbox is enabled.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onCheckedChange`

Supported platforms: Android.

Optional • Type: `(value: boolean) => void`

Callback function that is called when the checked state changes.

### `value`

Supported platforms: Android.

Type: `boolean`

Indicates whether the checkbox is checked.

### `TriStateCheckbox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TriStateCheckboxProps](#tristatecheckboxprops)\>

A tri-state checkbox component that supports `'on'`, `'off'`, and `'indeterminate'` states. Useful for "select all" patterns where the parent checkbox reflects the state of its children.

TriStateCheckboxProps

### `colors`

Supported platforms: Android.

Optional • Type: [CheckboxColors](/versions/v57.0.0/sdk/ui/jetpack-compose/checkbox.md#checkboxcolors)

Colors for checkbox core elements.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the checkbox is enabled.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback function that is called when the checkbox is clicked.

### `state`

Supported platforms: Android.

Type: [ToggleableState](#toggleablestate)

The toggleable state of the checkbox: `'on'`, `'off'`, or `'indeterminate'`.

## Types

### `CheckboxColors`

Supported platforms: Android.

Colors for checkbox core elements.

| Property | Type | Description |
| --- | --- | --- |
| checkedColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| checkmarkColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledCheckedColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledIndeterminateColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledUncheckedColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| uncheckedColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |

### `ToggleableState`

Supported platforms: Android.

Literal Type: `string`

The toggleable state of a tri-state checkbox.

Acceptable values are: `'on'` | `'off'` | `'indeterminate'`
