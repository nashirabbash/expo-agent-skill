---
title: "LazyVStack"
description: "A SwiftUI LazyVStack component for lazy vertical layouts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/lazyvstack.md"
scraped_at: "2026-07-15T08:59:33.525576"
---

---
title: LazyVStack
description: A SwiftUI LazyVStack component for lazy vertical layouts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# LazyVStack

A SwiftUI LazyVStack component for lazy vertical layouts.
iOS, tvOS, Included in Expo Go

Expo UI LazyVStack matches the official SwiftUI [LazyVStack API](https://developer.apple.com/documentation/swiftui/lazyvstack) and arranges its children vertically, creating items only as needed (when they become visible during scrolling).

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

### Basic lazy vertical stack

LazyVStack should be used inside a `ScrollView` to enable lazy rendering.

```tsx
import { Host, ScrollView, LazyVStack, Text } from '@expo/ui/swift-ui';

export default function BasicLazyVStackExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView>
        <LazyVStack spacing={12}>
          {Array.from({ length: 100 }, (_, i) => (
            <Text key={i}>{`Item ${i}`}</Text>
          ))}
        </LazyVStack>
      </ScrollView>
    </Host>
  );
}
```

### With alignment

The `alignment` prop controls horizontal alignment of children. Available options are: `leading`, `center`, and `trailing`.

```tsx
import { Host, ScrollView, LazyVStack, Rectangle } from '@expo/ui/swift-ui';
import { frame } from '@expo/ui/swift-ui/modifiers';

export default function LazyVStackAlignmentExample() {
  return (
    <Host style={{ flex: 1 }}>
      <ScrollView>
        <LazyVStack spacing={12} alignment="leading">
          <Rectangle modifiers={[frame({ width: 50, height: 50 })]} />
          <Rectangle modifiers={[frame({ width: 100, height: 50 })]} />
          <Rectangle modifiers={[frame({ width: 75, height: 50 })]} />
        </LazyVStack>
      </ScrollView>
    </Host>
  );
}
```

## API

```tsx
import { LazyVStack } from '@expo/ui/swift-ui';
```

## Component

### `LazyVStack`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[LazyVStackProps](#lazyvstackprops)\>

LazyVStackProps

### `alignment`

Supported platforms: iOS, tvOS.

Optional • Literal type: `string`

The horizontal alignment of children within the stack.

Acceptable values are: `'center'` | `'leading'` | `'trailing'`

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `spacing`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

The spacing between children.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
