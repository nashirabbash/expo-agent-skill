---
title: "VStack"
description: "A SwiftUI VStack component for vertical layouts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/vstack.md"
scraped_at: "2026-07-15T08:59:23.255067"
---

---
title: VStack
description: A SwiftUI VStack component for vertical layouts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# VStack

A SwiftUI VStack component for vertical layouts.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Column`](/versions/latest/sdk/ui/universal/column.md) — it renders the appropriate native component per platform.

Expo UI VStack matches the official SwiftUI [VStack API](https://developer.apple.com/documentation/swiftui/vstack) and arranges its children vertically.

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

### Basic vertical stack

```tsx
import { Host, VStack, Text } from '@expo/ui/swift-ui';

export default function BasicVStackExample() {
  return (
    <Host matchContents>
      <VStack spacing={12}>
        <Text>First</Text>
        <Text>Second</Text>
        <Text>Third</Text>
      </VStack>
    </Host>
  );
}
```

### With alignment

The `alignment` prop controls horizontal alignment of children. Available options are: `leading`, `center`, and `trailing`.

```tsx
import { Host, VStack, Rectangle } from '@expo/ui/swift-ui';
import { frame } from '@expo/ui/swift-ui/modifiers';

export default function VStackAlignmentExample() {
  return (
    <Host matchContents>
      <VStack spacing={12} alignment="leading">
        <Rectangle modifiers={[frame({ width: 50, height: 50 })]} />
        <Rectangle modifiers={[frame({ width: 100, height: 50 })]} />
        <Rectangle modifiers={[frame({ width: 75, height: 50 })]} />
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { VStack } from '@expo/ui/swift-ui';
```

## Component

### `VStack`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[VStackProps](#vstackprops)\>

VStackProps

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
