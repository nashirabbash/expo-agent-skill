---
title: "ExposedDropdownMenuBox"
description: "A Jetpack Compose ExposedDropdownMenuBox component for displaying a dropdown menu with a customizable anchor."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/exposeddropdownmenubox.md"
scraped_at: "2026-07-15T09:00:41.566686"
---

---
title: ExposedDropdownMenuBox
description: A Jetpack Compose ExposedDropdownMenuBox component for displaying a dropdown menu with a customizable anchor.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ExposedDropdownMenuBox

A Jetpack Compose ExposedDropdownMenuBox component for displaying a dropdown menu with a customizable anchor.
Android, Included in Expo Go

> For a cross-platform picker, see [`Picker`](/versions/latest/sdk/ui/universal/picker.md) — built on top of `ExposedDropdownMenuBox` on Android.

Expo UI `ExposedDropdownMenuBox` matches the official Jetpack Compose [`ExposedDropdownMenuBox`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-exposed-dropdown-menu-box.html). Use the `menuAnchor()` modifier on the anchor content (typically a read-only `TextField`) and `ExposedDropdownMenu` to wrap `DropdownMenuItem` children.

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

### Basic

> The anchor is a read-only `TextField` bound to a [`useNativeState`](/versions/latest/sdk/ui/jetpack-compose/usenativestate.md) observable. Update that observable in each item's `onClick` to reflect the selected value.

```tsx
import {
  DropdownMenuItem,
  ExposedDropdownMenuBox,
  ExposedDropdownMenu,
  Host,
  Text,
  TextField,
  useNativeState,
} from '@expo/ui/jetpack-compose';
import { menuAnchor } from '@expo/ui/jetpack-compose/modifiers';
import { useState } from 'react';

const LANGUAGES = [
  { label: 'Java', value: 'java' },
  { label: 'JavaScript', value: 'js' },
  { label: 'TypeScript', value: 'ts' },
];

export default function BasicExposedDropdownMenuBoxExample() {
  const selectedLabel = useNativeState('Java');
  const [expanded, setExpanded] = useState(false);

  return (
    <Host matchContents>
      <ExposedDropdownMenuBox expanded={expanded} onExpandedChange={setExpanded}>
        <TextField value={selectedLabel} readOnly modifiers={[menuAnchor()]} />
        <ExposedDropdownMenu expanded={expanded} onDismissRequest={() => setExpanded(false)}>
          {LANGUAGES.map(lang => (
            <DropdownMenuItem
              key={lang.value}
              onClick={() => {
                selectedLabel.value = lang.label;
                setExpanded(false);
              }}>
              <DropdownMenuItem.Text>
                <Text>{lang.label}</Text>
              </DropdownMenuItem.Text>
            </DropdownMenuItem>
          ))}
        </ExposedDropdownMenu>
      </ExposedDropdownMenuBox>
    </Host>
  );
}
```

## API

```tsx
import { ExposedDropdownMenuBox } from '@expo/ui/jetpack-compose';
```

## Components

### `ExposedDropdownMenu`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ExposedDropdownMenuProps](#exposeddropdownmenuprops)\>

A Material 3 `ExposedDropdownMenu` that displays menu items in a dropdown.

Must be used inside an `ExposedDropdownMenuBox`.

Props for the `ExposedDropdownMenu` component.

ExposedDropdownMenuProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children should be `DropdownMenuItem` components.

### `containerColor`

Supported platforms: Android.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

Background color of the dropdown menu container.

### `expanded`

Supported platforms: Android.

Type: `boolean`

Whether the dropdown menu is expanded (visible).

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onDismissRequest`

Supported platforms: Android.

Optional • Type: `() => void`

Callback fired when the menu requests to be dismissed (e.g. tapping outside, back button).

### `ExposedDropdownMenuBox`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ExposedDropdownMenuBoxProps](#exposeddropdownmenuboxprops)\>

A Material 3 `ExposedDropdownMenuBox`.

Use the `menuAnchor()` modifier on the anchor content (e.g. a `TextField` or `Text`). Use `ExposedDropdownMenu` to wrap `DropdownMenuItem` children.

Example

```tsx
<ExposedDropdownMenuBox expanded={expanded} onExpandedChange={setExpanded}>
  <TextField modifiers={[menuAnchor()]} defaultValue={value} readOnly />
  <ExposedDropdownMenu expanded={expanded} onDismissRequest={() => setExpanded(false)}>
    <DropdownMenuItem onClick={() => { setSelected('a'); setExpanded(false); }}>
      <DropdownMenuItem.Text><Text>Option A</Text></DropdownMenuItem.Text>
    </DropdownMenuItem>
  </ExposedDropdownMenu>
</ExposedDropdownMenuBox>
```

ExposedDropdownMenuBoxProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children — should contain an anchor element with the `menuAnchor()` modifier and an `ExposedDropdownMenu` with `DropdownMenuItem` children.

### `expanded`

Supported platforms: Android.

Type: `boolean`

Whether the dropdown menu is expanded (visible).

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onExpandedChange`

Supported platforms: Android.

Optional • Type: `(expanded: boolean) => void`

Callback when the expanded state changes (for example, tapping the field or dismissing the menu).
