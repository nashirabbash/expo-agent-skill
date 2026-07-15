---
title: "Column"
description: "A vertical layout container for universal @expo/ui components."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/column.md"
scraped_at: "2026-07-15T09:01:41.007308"
---

---
title: Column
description: A vertical layout container for universal @expo/ui components.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Column

A vertical layout container for universal @expo/ui components.
Android, iOS, Web, Included in Expo Go

A vertical layout container that arranges its children from top to bottom. Delegates to SwiftUI's [`VStack`](/versions/latest/sdk/ui/swift-ui/vstack.md) on iOS, Jetpack Compose's [`Column`](/versions/latest/sdk/ui/jetpack-compose/column.md) on Android, and a flex `View` on web.

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

### Basic column

```tsx
import { Host, Column, Text } from '@expo/ui';

export default function ColumnExample() {
  return (
    <Host matchContents>
      <Column spacing={8}>
        <Text>First</Text>
        <Text>Second</Text>
        <Text>Third</Text>
      </Column>
    </Host>
  );
}
```

### Alignment

Use [`alignment`](/versions/latest/sdk/ui/universal/column.md#alignment) to position children along the cross (horizontal) axis.

```tsx
import { Host, Column, Text } from '@expo/ui';

export default function ColumnAlignmentExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Column spacing={8} alignment="center">
        <Text>Centered</Text>
        <Text>Centered</Text>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { Column } from '@expo/ui';
```

## Component

### `Column`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ColumnProps](#columnprops)\>

A vertical layout container that arranges its children from top to bottom.

Props for the [`Column`](#column) component, a vertical layout container.

ColumnProps

### `alignment`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string` • Default: `'start'`

Cross-axis (horizontal) alignment of children.

Acceptable values are: `'start'` | `'center'` | `'end'`

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to render inside the column.

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

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

### `spacing`

Supported platforms: Android, iOS, Web.

Optional • Type: `number`

Vertical spacing between children, in density-independent pixels.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.
