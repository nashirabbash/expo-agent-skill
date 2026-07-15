---
title: "Slider"
description: "A control for selecting a value from a continuous or stepped range."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/slider.md"
scraped_at: "2026-07-15T09:01:42.587560"
---

---
title: Slider
description: A control for selecting a value from a continuous or stepped range.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Slider

A control for selecting a value from a continuous or stepped range.
Android, iOS, Web, Included in Expo Go

A controlled slider for selecting a numeric value within a range. Pair [`value`](/versions/latest/sdk/ui/universal/slider.md#value) with [`onValueChange`](/versions/latest/sdk/ui/universal/slider.md#onvaluechange) to manage state from React.

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

### Continuous slider

The default range is `[0, 1]`.

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui';

export default function ContinuousSliderExample() {
  const [value, setValue] = useState(0.5);

  return (
    <Host style={{ flex: 1 }}>
      <Slider value={value} onValueChange={setValue} />
    </Host>
  );
}
```

### Stepped slider with custom range

Use `min`, `max`, and `step` to constrain the values produced by the slider.

```tsx
import { useState } from 'react';
import { Host, Column, Slider, Text } from '@expo/ui';

export default function SteppedSliderExample() {
  const [volume, setVolume] = useState(50);

  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={8}>
        <Text>Volume: {volume}</Text>
        <Slider value={volume} onValueChange={setVolume} min={0} max={100} step={10} />
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Slider } from '@expo/ui';
```

## Component

### `Slider`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SliderProps](#sliderprops)\>

A control for selecting a value from a continuous or stepped range.

Props for the [`Slider`](#slider) component.

SliderProps

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the slider is disabled. Disabled sliders do not respond to user interaction.

### `max`

Supported platforms: Android, iOS, Web.

Optional • Type: `number` • Default: `1`

Maximum value of the slider range.

### `min`

Supported platforms: Android, iOS, Web.

Optional • Type: `number` • Default: `0`

Minimum value of the slider range.

### `modifiers`

Supported platforms: Android, iOS, Web.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`.

### `onValueChange`

Supported platforms: Android, iOS, Web.

Type: `(value: number) => void`

Called when the user changes the slider value.

### `step`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Increment size. For example, `step={10}` with `min={0}` and `max={100}` produces values `0, 10, 20, …, 100`.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `value`

Supported platforms: Android, iOS, Web.

Type: `number`

Current value of the slider.
