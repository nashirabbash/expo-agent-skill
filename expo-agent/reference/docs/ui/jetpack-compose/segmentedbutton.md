---
title: "SegmentedButton"
description: "Jetpack Compose Segmented Button components for single or multi-choice selection."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/segmentedbutton.md"
scraped_at: "2026-07-15T09:01:01.427750"
---

---
title: SegmentedButton
description: Jetpack Compose Segmented Button components for single or multi-choice selection.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# SegmentedButton

Jetpack Compose Segmented Button components for single or multi-choice selection.
Android, Included in Expo Go

Segmented buttons let app users choose from a small set of options displayed side by side in a row. They map to the official Jetpack Compose [Segmented Button](https://developer.android.com/develop/ui/compose/components/segmented-button) API.

There are two container types:

-   **`SingleChoiceSegmentedButtonRow`**: only one button can be selected at a time (like radio buttons).
-   **`MultiChoiceSegmentedButtonRow`**: multiple buttons can be toggled independently (like checkboxes).

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

### Single-choice segmented button

Use `SingleChoiceSegmentedButtonRow` when only one option can be active at a time. Each `SegmentedButton` takes `selected` and `onClick` props.

```tsx
import { useState } from 'react';
import {
  Host,
  SingleChoiceSegmentedButtonRow,
  SegmentedButton,
  Text,
} from '@expo/ui/jetpack-compose';

export default function SingleChoiceExample() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const options = ['Day', 'Week', 'Month', 'Year'];

  return (
    <Host matchContents>
      <SingleChoiceSegmentedButtonRow>
        {options.map((label, index) => (
          <SegmentedButton
            key={label}
            selected={index === selectedIndex}
            onClick={() => setSelectedIndex(index)}>
            <SegmentedButton.Label>
              <Text>{label}</Text>
            </SegmentedButton.Label>
          </SegmentedButton>
        ))}
      </SingleChoiceSegmentedButtonRow>
    </Host>
  );
}
```

### Multi-choice segmented button

Use `MultiChoiceSegmentedButtonRow` when multiple options can be toggled independently. Each `SegmentedButton` takes `checked` and `onCheckedChange` props.

```tsx
import { useState } from 'react';
import {
  Host,
  MultiChoiceSegmentedButtonRow,
  SegmentedButton,
  Text,
} from '@expo/ui/jetpack-compose';

export default function MultiChoiceExample() {
  const [checkedItems, setCheckedItems] = useState([false, false, false, false]);
  const options = ['Wi-Fi', 'Bluetooth', 'NFC', 'GPS'];

  return (
    <Host matchContents>
      <MultiChoiceSegmentedButtonRow>
        {options.map((label, index) => (
          <SegmentedButton
            key={label}
            checked={checkedItems[index]}
            onCheckedChange={checked => {
              setCheckedItems(prev => {
                const next = [...prev];
                next[index] = checked;
                return next;
              });
            }}>
            <SegmentedButton.Label>
              <Text>{label}</Text>
            </SegmentedButton.Label>
          </SegmentedButton>
        ))}
      </MultiChoiceSegmentedButtonRow>
    </Host>
  );
}
```

### Custom colors

Use the `colors` prop on `SegmentedButton` to customize its appearance across active, inactive, and disabled states.

```tsx
import { useState } from 'react';
import {
  Host,
  SingleChoiceSegmentedButtonRow,
  SegmentedButton,
  Text,
} from '@expo/ui/jetpack-compose';

export default function CustomColorsExample() {
  const [selectedIndex, setSelectedIndex] = useState(0);
  const options = ['$', '$$', '$$$', '$$$$'];

  return (
    <Host matchContents>
      <SingleChoiceSegmentedButtonRow>
        {options.map((label, index) => (
          <SegmentedButton
            key={label}
            selected={index === selectedIndex}
            onClick={() => setSelectedIndex(index)}
            colors={{
              activeContainerColor: '#6200EE',
              activeContentColor: '#FFFFFF',
            }}>
            <SegmentedButton.Label>
              <Text>{label}</Text>
            </SegmentedButton.Label>
          </SegmentedButton>
        ))}
      </SingleChoiceSegmentedButtonRow>
    </Host>
  );
}
```

## API

```tsx
import {
  SingleChoiceSegmentedButtonRow,
  MultiChoiceSegmentedButtonRow,
  SegmentedButton,
} from '@expo/ui/jetpack-compose';
```

## Components

### `MultiChoiceSegmentedButtonRow`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[MultiChoiceSegmentedButtonRowProps](#multichoicesegmentedbuttonrowprops)\>

A row container for multi-choice `SegmentedButton` children. Maps to Material 3 `MultiChoiceSegmentedButtonRow`.

MultiChoiceSegmentedButtonRowProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

SegmentedButton children.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `SegmentedButton`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SegmentedButtonProps](#segmentedbuttonprops)\>

A Material 3 segmented button. Must be used inside a `SingleChoiceSegmentedButtonRow` or `MultiChoiceSegmentedButtonRow`.

SegmentedButtonProps

### `checked`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the button is currently checked (used inside `MultiChoiceSegmentedButtonRow`).

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing a `Label` slot.

### `colors`

Supported platforms: Android.

Optional • Type: [SegmentedButtonColors](#segmentedbuttoncolors)

Colors for the button in different states.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the button is enabled.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onCheckedChange`

Supported platforms: Android.

Optional • Type: `(checked: boolean) => void`

Callback that is called when the checked state changes (used inside `MultiChoiceSegmentedButtonRow`).

### `onClick`

Supported platforms: Android.

Optional • Type: `() => void`

Callback that is called when the button is clicked (used inside `SingleChoiceSegmentedButtonRow`).

### `selected`

Supported platforms: Android.

Optional • Type: `boolean`

Whether the button is currently selected (used inside `SingleChoiceSegmentedButtonRow`).

### `SingleChoiceSegmentedButtonRow`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SingleChoiceSegmentedButtonRowProps](#singlechoicesegmentedbuttonrowprops)\>

A row container for single-choice `SegmentedButton` children. Maps to Material 3 `SingleChoiceSegmentedButtonRow`.

SingleChoiceSegmentedButtonRowProps

### `children`

Supported platforms: Android.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

SegmentedButton children.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

## Types

### `SegmentedButtonColors`

Supported platforms: Android.

Colors for the segmented button in different states.

| Property | Type | Description |
| --- | --- | --- |
| activeBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| activeContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| activeContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledActiveBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledActiveContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledActiveContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledInactiveBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledInactiveContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| disabledInactiveContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| inactiveBorderColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| inactiveContainerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| inactiveContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
