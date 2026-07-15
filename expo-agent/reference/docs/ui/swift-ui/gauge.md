---
title: "Gauge"
description: "A SwiftUI Gauge component for displaying progress with visual indicators."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/gauge.md"
scraped_at: "2026-07-15T08:59:11.217612"
---

---
title: Gauge
description: A SwiftUI Gauge component for displaying progress with visual indicators.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Gauge

A SwiftUI Gauge component for displaying progress with visual indicators.
iOS, Included in Expo Go

Expo UI Gauge matches the official SwiftUI [Gauge API](https://developer.apple.com/documentation/swiftui/gauge) and supports styling via the [`gaugeStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#gaugestylestyle) modifier.

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

### Basic gauge

```tsx
import { Host, Gauge } from '@expo/ui/swift-ui';

export default function BasicGaugeExample() {
  return (
    <Host matchContents>
      <Gauge value={0.5} />
    </Host>
  );
}
```

### With label

You can pass custom components as `children` to provide a label for the gauge.

```tsx
import { Host, Gauge, Text } from '@expo/ui/swift-ui';

export default function LabelExample() {
  return (
    <Host matchContents>
      <Gauge value={0.7}>
        <Text>Progress</Text>
      </Gauge>
    </Host>
  );
}
```

### With value labels

Use the `currentValueLabel`, `minimumValueLabel`, and `maximumValueLabel` props to display value information.

```tsx
import { Host, Gauge, Text } from '@expo/ui/swift-ui';

export default function ValueLabelsExample() {
  return (
    <Host matchContents>
      <Gauge
        value={50}
        min={0}
        max={100}
        currentValueLabel={<Text>50%</Text>}
        minimumValueLabel={<Text>0</Text>}
        maximumValueLabel={<Text>100</Text>}>
        <Text>Usage</Text>
      </Gauge>
    </Host>
  );
}
```

### Gauge styles

Use the `gaugeStyle` modifier to change the gauge's appearance. Available styles are: `automatic`, `circular`, `circularCapacity`, `linear`, and `linearCapacity`.

```tsx
import { Host, Gauge, Text, VStack } from '@expo/ui/swift-ui';
import { gaugeStyle } from '@expo/ui/swift-ui/modifiers';

export default function GaugeStylesExample() {
  return (
    <Host matchContents>
      <VStack spacing={16}>
        <Gauge value={0.5} modifiers={[gaugeStyle('circular')]}>
          <Text>Circular</Text>
        </Gauge>
        <Gauge value={0.5} modifiers={[gaugeStyle('circularCapacity')]}>
          <Text>Circular Capacity</Text>
        </Gauge>
        <Gauge value={0.5} modifiers={[gaugeStyle('linear')]}>
          <Text>Linear</Text>
        </Gauge>
        <Gauge value={0.5} modifiers={[gaugeStyle('linearCapacity')]}>
          <Text>Linear Capacity</Text>
        </Gauge>
      </VStack>
    </Host>
  );
}
```

### Tinted gauge

Use the `tint` modifier to change the gauge's color.

```tsx
import { Host, Gauge, VStack } from '@expo/ui/swift-ui';
import { gaugeStyle, tint } from '@expo/ui/swift-ui/modifiers';

export default function TintedGaugeExample() {
  return (
    <Host matchContents>
      <VStack spacing={16}>
        <Gauge value={0.7} modifiers={[gaugeStyle('circular'), tint('green')]} />
        <Gauge value={0.3} modifiers={[gaugeStyle('linear'), tint('red')]} />
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { Gauge } from '@expo/ui/swift-ui';
```

## Component

### `Gauge`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[GaugeProps](#gaugeprops)\>

Renders a SwiftUI `Gauge` component.

GaugeProps

### `children`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label describing the gauge's purpose.

### `currentValueLabel`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label showing the current value. Use `Text` or `Label` to display the value.

### `max`

Supported platforms: iOS.

Optional • Type: `number` • Default: `1`

The maximum value of the gauge range.

### `maximumValueLabel`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label showing the maximum value. Use `Text` or `Label` to display the value.

### `min`

Supported platforms: iOS.

Optional • Type: `number` • Default: `0`

The minimum value of the gauge range.

### `minimumValueLabel`

Supported platforms: iOS.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

A label showing the minimum value. Use `Text` or `Label` to display the value.

### `value`

Supported platforms: iOS.

Type: `number`

The current value of the gauge.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
