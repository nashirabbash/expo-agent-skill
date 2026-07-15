---
title: "ColorPicker"
description: "A SwiftUI ColorPicker component for selecting colors."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/colorpicker.md"
scraped_at: "2026-07-15T08:59:16.128559"
---

---
title: ColorPicker
description: A SwiftUI ColorPicker component for selecting colors.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ColorPicker

A SwiftUI ColorPicker component for selecting colors.
iOS, Included in Expo Go

Expo UI ColorPicker matches the official SwiftUI [ColorPicker API](https://developer.apple.com/documentation/swiftui/colorpicker) and allows app users to select colors from a palette.

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

### Basic color picker

```tsx
import { useState } from 'react';
import { Host, ColorPicker } from '@expo/ui/swift-ui';

export default function ColorPickerExample() {
  const [color, setColor] = useState('#FF6347');

  return (
    <Host matchContents>
      <ColorPicker label="Select a color" selection={color} onSelectionChange={setColor} />
    </Host>
  );
}
```

### Color picker with opacity support

Use the `supportsOpacity` prop to allow users to select colors with alpha transparency.

```tsx
import { useState } from 'react';
import { Host, ColorPicker } from '@expo/ui/swift-ui';

export default function ColorPickerOpacityExample() {
  const [color, setColor] = useState('#FF634780');

  return (
    <Host matchContents>
      <ColorPicker
        label="Select a color with opacity"
        selection={color}
        onSelectionChange={setColor}
        supportsOpacity
      />
    </Host>
  );
}
```

## API

```tsx
import { ColorPicker } from '@expo/ui/swift-ui';
```

## Component

### `ColorPicker`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ColorPickerProps](#colorpickerprops)\>

Renders a `ColorPicker` component using SwiftUI.

ColorPickerProps

### `label`

Supported platforms: iOS.

Optional • Type: `string`

A label displayed on the `ColorPicker`.

### `onSelectionChange`

Supported platforms: iOS.

Optional • Type: `(value: string) => void`

Callback function that is called when a new color is selected.

### `selection`

Supported platforms: iOS.

Literal type: `union`

The currently selected color in the format `#RRGGBB` or `#RRGGBBAA`.

Acceptable values are: `string` | `null`

### `supportsOpacity`

Supported platforms: iOS.

Optional • Type: `boolean`

Whether the color picker should support opacity.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
