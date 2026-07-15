---
title: "ToggleButton"
description: "Jetpack Compose ToggleButton components for displaying native Material3 toggle buttons."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/togglebutton.md"
scraped_at: "2026-07-15T09:00:55.436960"
---

---
title: ToggleButton
description: Jetpack Compose ToggleButton components for displaying native Material3 toggle buttons.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ToggleButton

Jetpack Compose ToggleButton components for displaying native Material3 toggle buttons.
Android, Included in Expo Go

Expo UI provides four toggle button components that match the official Jetpack Compose Toggle Button API: [`ToggleButton`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-toggle-button.html), [`IconToggleButton`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-icon-toggle-button.html), [`FilledIconToggleButton`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-filled-icon-toggle-button.html), and [`OutlinedIconToggleButton`](https://kotlinlang.org/api/compose-multiplatform/material3/androidx.compose.material3/-outlined-icon-toggle-button.html).

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

### Basic toggle button

A toggle button with text and icon content.

```tsx
import { useState } from 'react';
import { Host, ToggleButton, Text } from '@expo/ui/jetpack-compose';

export default function BasicToggleButtonExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <ToggleButton checked={checked} onCheckedChange={setChecked}>
        <Text>Favorite</Text>
      </ToggleButton>
    </Host>
  );
}
```

### Icon toggle button variants

Use different icon toggle button components to convey varying levels of emphasis.

```tsx
import { useState } from 'react';
import {
  Host,
  IconToggleButton,
  FilledIconToggleButton,
  OutlinedIconToggleButton,
  Icon,
  Row,
} from '@expo/ui/jetpack-compose';

const starIcon = require('./assets/star.png');

export default function IconToggleButtonVariantsExample() {
  const [checked1, setChecked1] = useState(false);
  const [checked2, setChecked2] = useState(true);
  const [checked3, setChecked3] = useState(false);

  return (
    <Host matchContents>
      <Row horizontalArrangement={{ spacedBy: 8 }}>
        <IconToggleButton checked={checked1} onCheckedChange={setChecked1}>
          <Icon source={starIcon} size={24} />
        </IconToggleButton>
        <FilledIconToggleButton checked={checked2} onCheckedChange={setChecked2}>
          <Icon source={starIcon} size={24} />
        </FilledIconToggleButton>
        <OutlinedIconToggleButton checked={checked3} onCheckedChange={setChecked3}>
          <Icon source={starIcon} size={24} />
        </OutlinedIconToggleButton>
      </Row>
    </Host>
  );
}
```

### Custom colors

Override checked and unchecked colors using the `colors` prop.

```tsx
import { useState } from 'react';
import { Host, ToggleButton, Text } from '@expo/ui/jetpack-compose';

export default function CustomColorsToggleButtonExample() {
  const [checked, setChecked] = useState(true);

  return (
    <Host matchContents>
      <ToggleButton
        checked={checked}
        onCheckedChange={setChecked}
        colors={{
          checkedContainerColor: '#4CAF50',
          checkedContentColor: '#FFFFFF',
          containerColor: '#E0E0E0',
          contentColor: '#333333',
        }}>
        <Text>{checked ? 'ON' : 'OFF'}</Text>
      </ToggleButton>
    </Host>
  );
}
```

### Disabled toggle button

```tsx
import { Host, ToggleButton, Text } from '@expo/ui/jetpack-compose';

export default function DisabledToggleButtonExample() {
  return (
    <Host matchContents>
      <ToggleButton checked={false} enabled={false}>
        <Text>Disabled</Text>
      </ToggleButton>
    </Host>
  );
}
```

## API

```tsx
import {
  ToggleButton,
  IconToggleButton,
  FilledIconToggleButton,
  OutlinedIconToggleButton,
} from '@expo/ui/jetpack-compose';
```

## Components

### `FilledIconToggleButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ToggleButtonProps](#togglebuttonprops)\>

A filled icon toggle button with a solid background.

### `IconToggleButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ToggleButtonProps](#togglebuttonprops)\>

An icon toggle button with no background.

### `OutlinedIconToggleButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ToggleButtonProps](#togglebuttonprops)\>

An outlined icon toggle button with a border and no fill.

### `ToggleButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ToggleButtonProps](#togglebuttonprops)\>

A toggle button component that can be toggled on and off.

ToggleButtonProps

### `checked`

Supported platforms: Android.

Type: `boolean`

Whether the toggle button is checked.

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to display inside the toggle button.

### `colors`

Supported platforms: Android.

Optional • Type: [ToggleButtonColors](#togglebuttoncolors)

Colors for toggle button elements.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the button is enabled for user interaction.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onCheckedChange`

Supported platforms: Android.

Optional • Type: `(checked: boolean) => void`

Callback that is called when the checked state changes.

### `ToggleButton.DefaultIconSize`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<number\>

## Types

### `ToggleButtonColors`

Supported platforms: Android.

Colors for toggle button elements.

| Property | Type | Description |
| --- | --- | --- |
| checkedContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| checkedContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| contentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
