---
title: "Spacer"
description: "A Jetpack Compose Spacer component for adding flexible space between elements."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/spacer.md"
scraped_at: "2026-07-15T09:00:23.941673"
---

---
title: Spacer
description: A Jetpack Compose Spacer component for adding flexible space between elements.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Spacer

A Jetpack Compose Spacer component for adding flexible space between elements.
Android, Included in Expo Go

> For cross-platform usage, see the universal [`Spacer`](/versions/latest/sdk/ui/universal/spacer.md) — it renders the appropriate native component per platform.

Expo UI Spacer matches the official Jetpack Compose [Spacer](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Spacer) API and is used to add flexible or fixed-size space between elements in a layout.

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

### Spacer with weight

Use the `weight()` modifier to make the spacer fill available space proportionally within a `Row` or `Column`.

```tsx
import { Host, Row, Spacer, Text } from '@expo/ui/jetpack-compose';
import { fillMaxWidth, weight } from '@expo/ui/jetpack-compose/modifiers';

export default function SpacerWeightExample() {
  return (
    <Host matchContents>
      <Row modifiers={[fillMaxWidth()]}>
        <Text>Left</Text>
        <Spacer modifiers={[weight(1)]} />
        <Text>Right</Text>
      </Row>
    </Host>
  );
}
```

### Spacer with fixed size

Use a `height` or `width` modifier to create a spacer with a fixed dimension.

```tsx
import { Host, Column, Spacer, Text } from '@expo/ui/jetpack-compose';
import { height } from '@expo/ui/jetpack-compose/modifiers';

export default function SpacerFixedSizeExample() {
  return (
    <Host matchContents>
      <Column>
        <Text>Above</Text>
        <Spacer modifiers={[height(24)]} />
        <Text>Below (24dp gap)</Text>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Spacer } from '@expo/ui/jetpack-compose';
```

## Component

### `Spacer`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SpacerProps](#spacerprops)\>

A spacer component that fills available space. Use with the `weight()` modifier to create flexible spacing in `Row` or `Column` layouts.

Example

```tsx
<Row>
  <Text>Left</Text>
  <Spacer modifiers={[weight(1)]} />
  <Text>Right</Text>
</Row>
```

SpacerProps

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component. Use `weight()` modifier to make the spacer flexible.
