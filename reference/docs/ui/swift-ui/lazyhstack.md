---
title: "LazyHStack"
description: "A SwiftUI LazyHStack component for lazy horizontal layouts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/lazyhstack.md"
scraped_at: "2026-07-15T08:59:40.664897"
---

---
title: LazyHStack
description: A SwiftUI LazyHStack component for lazy horizontal layouts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# LazyHStack

A SwiftUI LazyHStack component for lazy horizontal layouts.
iOS, tvOS, Included in Expo Go

Expo UI LazyHStack matches the official SwiftUI [LazyHStack API](https://developer.apple.com/documentation/swiftui/lazyhstack) and arranges its children horizontally, creating items only as needed (when they become visible during scrolling).

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

### Basic lazy horizontal stack

LazyHStack should be used inside a `ScrollView` with `axes="horizontal"` to enable lazy rendering.

```tsx
import { Host, ScrollView, LazyHStack, Text } from '@expo/ui/swift-ui';

export default function BasicLazyHStackExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView axes="horizontal">
        <LazyHStack spacing={12}>
          {Array.from({ length: 100 }, (_, i) => (
            <Text key={i}>{`Item ${i}`}</Text>
          ))}
        </LazyHStack>
      </ScrollView>
    </Host>
  );
}
```

### With alignment

The `alignment` prop controls vertical alignment of children. Available options are: `top`, `center`, `bottom`, `firstTextBaseline`, and `lastTextBaseline`.

```tsx
import { Host, ScrollView, LazyHStack, Rectangle } from '@expo/ui/swift-ui';
import { frame } from '@expo/ui/swift-ui/modifiers';

export default function LazyHStackAlignmentExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView axes="horizontal">
        <LazyHStack spacing={12} alignment="top">
          <Rectangle modifiers={[frame({ width: 50, height: 50 })]} />
          <Rectangle modifiers={[frame({ width: 50, height: 100 })]} />
          <Rectangle modifiers={[frame({ width: 50, height: 75 })]} />
        </LazyHStack>
      </ScrollView>
    </Host>
  );
}
```

## API

```tsx
import { LazyHStack } from '@expo/ui/swift-ui';
```

## Component

### `LazyHStack`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LazyHStackProps](#lazyhstackprops)\>

LazyHStackProps

### `alignment`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

The vertical alignment of children within the stack.

Acceptable values are: `'center'` | `'top'` | `'bottom'` | `'firstTextBaseline'` | `'lastTextBaseline'`

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `spacing`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

The spacing between children.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
