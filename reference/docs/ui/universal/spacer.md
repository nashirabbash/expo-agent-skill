---
title: "Spacer"
description: "A layout spacer that produces empty space between siblings."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/spacer.md"
scraped_at: "2026-07-15T09:01:48.918918"
---

---
title: Spacer
description: A layout spacer that produces empty space between siblings.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Spacer

A layout spacer that produces empty space between siblings.
Android, iOS, Web, Included in Expo Go

A layout spacer that produces empty space between siblings inside a [`Row`](/versions/latest/sdk/ui/universal/row.md) or [`Column`](/versions/latest/sdk/ui/universal/column.md). Use [`size`](/versions/latest/sdk/ui/universal/spacer.md#size) for a fixed gap, or [`flexible`](/versions/latest/sdk/ui/universal/spacer.md#flexible) to fill the remaining main-axis space.

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

### Fixed-size spacer

```tsx
import { Host, Column, Text, Spacer } from '@expo/ui';

export default function FixedSpacerExample() {
  return (
    <Host matchContents>
      <Column>
        <Text>Top</Text>
        <Spacer size={32} />
        <Text>Bottom</Text>
      </Column>
    </Host>
  );
}
```

### Flexible spacer

A flexible spacer fills the remaining space along its parent's main axis, pushing the surrounding content to opposite ends.

```tsx
import { Host, Row, Text, Spacer } from '@expo/ui';

export default function FlexibleSpacerExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Row>
        <Text>Leading</Text>
        <Spacer flexible />
        <Text>Trailing</Text>
      </Row>
    </Host>
  );
}
```

## API

```tsx
import { Spacer } from '@expo/ui';
```

## Component

### `Spacer`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SpacerProps](#spacerprops)\>

A layout spacer that produces empty space between siblings in a `Row` or `Column`.

Props for the [`Spacer`](#spacer) component.

A Spacer produces empty space between siblings in a `Row` or `Column`. Use `size` for a fixed amount of space, or `flexible` to fill the remaining space along the parent's main axis.

SpacerProps

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `flexible`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean` • Default: `false`

When `true`, the spacer expands to fill the available space along the parent's main axis, pushing sibling content to the opposite end.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is pressed.

### `size`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Fixed size in density-independent pixels. Interpreted as width in a horizontal container and as height in a vertical container.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.
