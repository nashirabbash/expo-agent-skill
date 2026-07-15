---
title: "Row"
description: "A horizontal layout container for universal @expo/ui components."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/row.md"
scraped_at: "2026-07-15T09:01:49.794620"
---

---
title: Row
description: A horizontal layout container for universal @expo/ui components.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Row

A horizontal layout container for universal @expo/ui components.
Android, iOS, Web, Included in Expo Go

A horizontal layout container that arranges its children from start to end. Delegates to Jetpack Compose's [`Row`](/versions/latest/sdk/ui/jetpack-compose/row.md) on Android, SwiftUI's [`HStack`](/versions/latest/sdk/ui/swift-ui/hstack.md) on iOS, and a flex `View` on web.

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

### Basic row

```tsx
import { Host, Row, Text } from '@expo/ui';

export default function RowExample() {
  return (
    <Host matchContents>
      <Row spacing={8}>
        <Text>One</Text>
        <Text>Two</Text>
        <Text>Three</Text>
      </Row>
    </Host>
  );
}
```

### Alignment

Use [`alignment`](/versions/latest/sdk/ui/universal/row.md#alignment) to position children along the cross (vertical) axis.

```tsx
import { Host, Row, Text } from '@expo/ui';

export default function RowAlignmentExample() {
  return (
    <Host style={{ flex: 1 }}>
      <Row spacing={8} alignment="center">
        <Text>Centered</Text>
        <Text>Centered</Text>
      </Row>
    </Host>
  );
}
```

### Pushing content apart with Spacer

Pair `Row` with a flexible [`Spacer`](/versions/latest/sdk/ui/universal/spacer.md) to push its children to the opposite ends.

```tsx
import { Host, Row, Text, Spacer } from '@expo/ui';

export default function RowSpacerExample() {
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
import { Row } from '@expo/ui';
```

## Component

### `Row`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RowProps](#rowprops)\>

A horizontal layout container that arranges its children from start to end.

Props for the [`Row`](#row) component, a horizontal layout container.

RowProps

### `alignment`

Supported platforms: Android, iOS, Web.

Optional • Literal type: `string` • Default: `'start'`

Cross-axis (vertical) alignment of children.

Acceptable values are: `'start'` | `'center'` | `'end'`

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content to render inside the row.

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

Horizontal spacing between children, in density-independent pixels.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.
