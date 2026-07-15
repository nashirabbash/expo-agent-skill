---
title: "Slider"
description: "A SwiftUI Slider component for selecting values from a range."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/slider.md"
scraped_at: "2026-07-15T08:59:30.119683"
---

---
title: Slider
description: A SwiftUI Slider component for selecting values from a range.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Slider

A SwiftUI Slider component for selecting values from a range.
iOS, Included in Expo Go

> For cross-platform usage, see the universal [`Slider`](/versions/latest/sdk/ui/universal/slider.md) — it renders the appropriate native component per platform.

Expo UI Slider matches the official SwiftUI [Slider API](https://developer.apple.com/documentation/swiftui/slider) and allows selecting values from a bounded range.

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

> **Note:** `Slider` is a flexible-width component, it expands to fill available horizontal space and does not have an intrinsic width. When using `matchContents` on the `Host`, you should apply a [`frame`](/versions/latest/sdk/ui/swift-ui/modifiers.md#frameparams) modifier on the `Slider` to give it an explicit width. Alternatively, give the `Host` an explicit size using `style` (for example, `style={{ width: 300 }}` or `style={{ flex: 1 }}`), or place the `Slider` inside a SwiftUI container like `Form` that provides width constraints.

### Basic slider

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/swift-ui';

export default function BasicSliderExample() {
  const [value, setValue] = useState(0.5);

  return (
    <Host style={{ flex: 1 }}>
      <Slider value={value} onValueChange={setValue} />
    </Host>
  );
}
```

### Slider with custom range

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/swift-ui';

export default function CustomRangeSliderExample() {
  const [value, setValue] = useState(50);

  return (
    <Host style={{ flex: 1 }}>
      <Slider value={value} min={0} max={100} onValueChange={setValue} />
    </Host>
  );
}
```

### Slider with step

Use the `step` prop to define discrete increments. Set `step` to `0` for continuous values.

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/swift-ui';

export default function SteppedSliderExample() {
  const [value, setValue] = useState(0);

  return (
    <Host style={{ flex: 1 }}>
      <Slider value={value} min={0} max={100} step={10} onValueChange={setValue} />
    </Host>
  );
}
```

### Slider with labels

You can add labels to describe a slider's purpose and to mark the minimum and maximum value positions.

```tsx
import { useState } from 'react';
import { Host, Slider, Text } from '@expo/ui/swift-ui';

export default function LabeledSliderExample() {
  const [value, setValue] = useState(50);

  return (
    <Host style={{ flex: 1 }}>
      <Slider
        value={value}
        min={0}
        max={100}
        label={<Text>Volume</Text>}
        minimumValueLabel={<Text>0</Text>}
        maximumValueLabel={<Text>100</Text>}
        onValueChange={setValue}
      />
    </Host>
  );
}
```

## API

```tsx
import { Slider } from '@expo/ui/swift-ui';
```

## Component

### `Slider`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SliderProps](#sliderprops)\>

SliderProps

### `label`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label describing the slider's purpose.

### `lowerLimit`

Supported platforms: iOS.

Optional • Type: `number`

Lower limit the user can drag the thumb to. The visible track still spans `min..max`, but the thumb stops at `lowerLimit` during drag.

### `max`

Supported platforms: iOS.

Optional • Type: `number`

The maximum value of the slider. Updating this value does not trigger callbacks if the current value is above `max`.

### `maximumValueLabel`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label displayed at the maximum value position.

### `min`

Supported platforms: iOS.

Optional • Type: `number`

The minimum value of the slider. Updating this value does not trigger callbacks if the current value is below `min`.

### `minimumValueLabel`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label displayed at the minimum value position.

### `onEditingChanged`

Supported platforms: iOS.

Optional • Type: `(isEditing: boolean) => void`

Callback triggered when the user starts or ends editing the slider.

### `onValueChange`

Supported platforms: iOS.

Optional • Type: `(value: number) => void`

Callback triggered on dragging along the slider.

### `step`

Supported platforms: iOS.

Optional • Type: `number`

The step increment for the slider.

### `upperLimit`

Supported platforms: iOS.

Optional • Type: `number`

Upper limit the user can drag the thumb to. The visible track still spans `min..max`, but the thumb stops at `upperLimit` during drag.

### `value`

Supported platforms: iOS.

Optional • Type: `number`

The current value of the slider.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
