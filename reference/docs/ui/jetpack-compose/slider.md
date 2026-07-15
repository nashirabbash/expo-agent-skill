---
title: "Slider"
description: "A Jetpack Compose Slider component for selecting values from a range."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/slider.md"
scraped_at: "2026-07-15T09:00:32.217124"
---

---
title: Slider
description: A Jetpack Compose Slider component for selecting values from a range.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Slider

A Jetpack Compose Slider component for selecting values from a range.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Slider`](/versions/latest/sdk/ui/universal/slider.md) — it renders the appropriate native component per platform.

Expo UI Slider matches the official Jetpack Compose [Slider API](https://developer.android.com/develop/ui/compose/components/slider) and allows selecting values from a bounded range.

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

### Basic slider

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/jetpack-compose';

export default function BasicSliderExample() {
  const [value, setValue] = useState(0.5);

  return (
    <Host matchContents>
      <Slider value={value} onValueChange={setValue} />
    </Host>
  );
}
```

### Slider with custom range

Use the `min` and `max` props to define the slider's value range.

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/jetpack-compose';

export default function CustomRangeSliderExample() {
  const [value, setValue] = useState(50);

  return (
    <Host matchContents>
      <Slider value={value} min={0} max={100} onValueChange={setValue} />
    </Host>
  );
}
```

### Slider with steps

Use the `steps` prop to define discrete increments. Set `steps` to `0` for continuous values.

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/jetpack-compose';

export default function SteppedSliderExample() {
  const [value, setValue] = useState(0);

  return (
    <Host matchContents>
      <Slider value={value} min={0} max={100} steps={10} onValueChange={setValue} />
    </Host>
  );
}
```

### Custom colors

Use the `colors` prop to override the default Material3 colors for the slider's thumb, track, and tick marks.

```tsx
import { useState } from 'react';
import { Host, Slider } from '@expo/ui/jetpack-compose';

export default function CustomColorsSliderExample() {
  const [value, setValue] = useState(0.5);

  return (
    <Host matchContents>
      <Slider
        value={value}
        colors={{
          thumbColor: '#6200EE',
          activeTrackColor: '#6200EE',
          inactiveTrackColor: '#E0E0E0',
        }}
        onValueChange={setValue}
      />
    </Host>
  );
}
```

### Custom thumb and track

Use both `Slider.Thumb` and `Slider.Track` slots for a fully custom slider appearance.

```tsx
import { useState } from 'react';
import { Host, Slider, Shape, Row, Box } from '@expo/ui/jetpack-compose';
import {
  fillMaxWidth,
  height,
  weight,
  size,
  clip,
  background,
  Shapes,
} from '@expo/ui/jetpack-compose/modifiers';

export default function FullyCustomSliderExample() {
  const [value, setValue] = useState(0.5);

  return (
    <Host matchContents>
      <Slider value={value} onValueChange={setValue}>
        <Slider.Thumb>
          <Box modifiers={[size(24, 24), clip(Shapes.Circle), background('#6200EE')]} />
        </Slider.Thumb>
        <Slider.Track>
          <Row modifiers={[fillMaxWidth(), height(8)]}>
            <Shape.RoundedCorner
              color="#6200EE"
              cornerRadii={{ topStart: 4, bottomStart: 4 }}
              modifiers={[weight(Math.max(value, 0.01)), height(8)]}
            />
            <Shape.RoundedCorner
              color="#BDBDBD"
              cornerRadii={{ topEnd: 4, bottomEnd: 4 }}
              modifiers={[weight(Math.max(1 - value, 0.01)), height(8)]}
            />
          </Row>
        </Slider.Track>
      </Slider>
    </Host>
  );
}
```

## API

```tsx
import { Slider } from '@expo/ui/jetpack-compose';
```

## Component

### `Slider`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SliderProps](#sliderprops)\>

A slider component that wraps Material3's `Slider`.

SliderProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Slot children for custom thumb and track.

### `colors`

Supported platforms: Android.

Optional • Type: [SliderColors](#slidercolors)

Colors for slider elements. Maps to Material3's `SliderDefaults.colors()`.

### `enabled`

Supported platforms: Android.

Optional • Type: `boolean` • Default: `true`

Whether the slider is enabled for user interaction.

### `lowerLimit`

Supported platforms: Android.

Optional • Type: `number`

Lower limit the user can drag the thumb to. The visible track still spans `min..max`, but the thumb stops at `lowerLimit` during drag.

### `max`

Supported platforms: Android.

Optional • Type: `number` • Default: `1`

The maximum value of the slider. Updating this value does not trigger callbacks if the current value is above `max`.

### `min`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

The minimum value of the slider. Updating this value does not trigger callbacks if the current value is below `min`.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `onValueChange`

Supported platforms: Android.

Optional • Type: `(value: number) => void`

Callback triggered on dragging along the slider.

### `onValueChangeFinished`

Supported platforms: Android.

Optional • Type: `() => void`

Callback triggered when the user finishes changing the value (for example, lifts a finger). Maps to Material3's `onValueChangeFinished`.

### `steps`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

The number of steps between the minimum and maximum values, `0` signifies infinite steps.

### `upperLimit`

Supported platforms: Android.

Optional • Type: `number`

Upper limit the user can drag the thumb to. The visible track still spans `min..max`, but the thumb stops at `upperLimit` during drag.

### `value`

Supported platforms: Android.

Optional • Type: `number` • Default: `0`

The current value of the slider.

## Types

### `SliderColors`

Supported platforms: Android.

Colors for slider elements. Maps directly to Material3's `SliderDefaults.colors()`.

| Property | Type | Description |
| --- | --- | --- |
| activeTickColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| activeTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| inactiveTickColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| inactiveTrackColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| thumbColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
