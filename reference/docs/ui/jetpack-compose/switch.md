---
title: "Switch"
description: "A Jetpack Compose Switch component for toggle controls."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/switch.md"
scraped_at: "2026-07-15T09:00:48.248420"
---

---
title: Switch
description: A Jetpack Compose Switch component for toggle controls.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Switch

A Jetpack Compose Switch component for toggle controls.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Switch`](/versions/latest/sdk/ui/universal/switch.md) — it renders the appropriate native component per platform.

Expo UI Switch matches the official Jetpack Compose [Switch](https://developer.android.com/develop/ui/compose/components/switch) API.

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

### Toggle switch

```tsx
import { useState } from 'react';
import { Host, Switch } from '@expo/ui/jetpack-compose';

export default function ToggleSwitchExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <Switch value={checked} onCheckedChange={setChecked} />
    </Host>
  );
}
```

### Custom colors

```tsx
import { useState } from 'react';
import { Host, Switch } from '@expo/ui/jetpack-compose';

export default function CustomColorsExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <Switch
        value={checked}
        onCheckedChange={setChecked}
        colors={{
          checkedThumbColor: '#6200EE',
          checkedTrackColor: '#EDE9FE',
          uncheckedThumbColor: '#9CA3AF',
          uncheckedTrackColor: '#F3F4F6',
          uncheckedBorderColor: '#D1D5DB',
        }}
      />
    </Host>
  );
}
```

### Custom thumb content

Use `Switch.ThumbContent` to render a custom element inside the thumb. `Switch.DefaultIconSize` gives you the M3 default icon size so your content fits perfectly.

```tsx
import { useState } from 'react';
import { Host, Switch, Box } from '@expo/ui/jetpack-compose';
import { size, clip, background, Shapes } from '@expo/ui/jetpack-compose/modifiers';

export default function ThumbContentExample() {
  const [checked, setChecked] = useState(false);

  return (
    <Host matchContents>
      <Switch
        value={checked}
        onCheckedChange={setChecked}
        colors={{
          checkedThumbColor: '#7C3AED',
          checkedTrackColor: '#EDE9FE',
          checkedIconColor: '#7C3AED',
          uncheckedThumbColor: '#9CA3AF',
          uncheckedTrackColor: '#F3F4F6',
          uncheckedBorderColor: '#D1D5DB',
          uncheckedIconColor: '#9CA3AF',
        }}>
        <Switch.ThumbContent>
          <Box
            modifiers={[
              size(Switch.DefaultIconSize, Switch.DefaultIconSize),
              clip(Shapes.Circle),
              background(checked ? '#FFFFFF' : '#E5E7EB'),
            ]}
          />
        </Switch.ThumbContent>
      </Switch>
    </Host>
  );
}
```

## API

```tsx
import { Switch } from '@expo/ui/jetpack-compose';
```

## Components

### `Switch`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SwitchProps](#switchprops)\>

A switch component.

SwitchProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing ThumbContent slot.

### `colors`

Supported platforms: Android.

Optional • Type: [SwitchColors](/versions/v57.0.0/sdk/ui/jetpack-compose/switch.md#switchcolors)

Colors for switch core elements.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the switch is enabled.

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

Indicates whether the switch is checked.

### `SwitchThumbContent`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ThumbContentProps\>

Custom content to be displayed inside the switch thumb.

## Types

### `SwitchColors`

Supported platforms: Android.

Colors for switch core elements.

| Property | Type | Description |
| --- | --- | --- |
| checkedBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| checkedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| checkedThumbColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| checkedTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledCheckedBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledCheckedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledCheckedThumbColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledCheckedTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledUncheckedBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledUncheckedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledUncheckedThumbColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledUncheckedTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| uncheckedBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| uncheckedIconColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| uncheckedThumbColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| uncheckedTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
