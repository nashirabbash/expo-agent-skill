---
title: "Divider"
description: "Jetpack Compose Divider components for creating visual separators."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/divider.md"
scraped_at: "2026-07-15T09:00:24.612073"
---

---
title: Divider
description: Jetpack Compose Divider components for creating visual separators.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Divider

Jetpack Compose Divider components for creating visual separators.
Android, Included in Expo Go

Expo UI provides [`HorizontalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#HorizontalDivider\(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color\)) and [`VerticalDivider`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#VerticalDivider\(androidx.compose.ui.Modifier,androidx.compose.ui.unit.Dp,androidx.compose.ui.graphics.Color\)) matching the official Jetpack Compose Divider API.

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

### Horizontal divider

A thin horizontal line to visually separate content in lists and layouts.

```tsx
import { Host, HorizontalDivider, Column, Text } from '@expo/ui/jetpack-compose';

export default function HorizontalDividerExample() {
  return (
    <Host matchContents>
      <Column>
        <Text>First section</Text>
        <HorizontalDivider />
        <Text>Second section</Text>
      </Column>
    </Host>
  );
}
```

### Custom thickness and color

Both `HorizontalDivider` and `VerticalDivider` accept `thickness` and `color` props. Use `StyleSheet.hairlineWidth` for a single-pixel line, or set a custom thickness and color.

```tsx
import { Host, HorizontalDivider, Column, Text } from '@expo/ui/jetpack-compose';
import { StyleSheet } from 'react-native';

export default function CustomDividerExample() {
  return (
    <Host matchContents>
      <Column>
        <Text>Hairline divider (1 pixel)</Text>
        <HorizontalDivider thickness={StyleSheet.hairlineWidth} />
        <Text>Thick colored divider</Text>
        <HorizontalDivider thickness={4} color="#E91E63" />
        <Text>Below</Text>
      </Column>
    </Host>
  );
}
```

### Vertical divider

A vertical line to separate items side by side in a row layout.

```tsx
import { Host, VerticalDivider, Row, Text } from '@expo/ui/jetpack-compose';
import { height } from '@expo/ui/jetpack-compose/modifiers';

export default function VerticalDividerExample() {
  return (
    <Host matchContents>
      <Row verticalAlignment="center" modifiers={[height(48)]}>
        <Text>Left</Text>
        <VerticalDivider />
        <Text>Right</Text>
      </Row>
    </Host>
  );
}
```

## API

```tsx
import { HorizontalDivider, VerticalDivider } from '@expo/ui/jetpack-compose';
```

## Components

### `HorizontalDivider`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[DividerCommonConfig](#dividercommonconfig)\>\>

A horizontal divider line that groups content in lists and layouts, matching Compose's `HorizontalDivider`.

### `VerticalDivider`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<ComponentType<[DividerCommonConfig](#dividercommonconfig)\>\>

A vertical divider line that groups content in layouts, matching Compose's `VerticalDivider`.

## Types

### `DividerCommonConfig`

Supported platforms: Android.

| Property | Type | Description |
| --- | --- | --- |
| color(optional) | [ColorValue](https://reactnative.dev/docs/colors) | Color of the divider line. |
| modifiers(optional) | `ModifierConfig[]` | Modifiers for the component. |
| thickness(optional) | `number` | Thickness of the divider line. Accepts dp values; use `StyleSheet.hairlineWidth` for a single-pixel line. |
