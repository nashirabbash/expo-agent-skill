---
title: "HStack"
description: "A SwiftUI HStack component for horizontal layouts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/hstack.md"
scraped_at: "2026-07-15T08:59:39.854483"
---

---
title: HStack
description: A SwiftUI HStack component for horizontal layouts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# HStack

A SwiftUI HStack component for horizontal layouts.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Row`](/versions/latest/sdk/ui/universal/row.md) — it renders the appropriate native component per platform.

Expo UI HStack matches the official SwiftUI [HStack API](https://developer.apple.com/documentation/swiftui/hstack) and arranges its children horizontally.

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

### Basic horizontal stack

```tsx
import { Host, HStack, Text } from '@expo/ui/swift-ui';

export default function BasicHStackExample() {
  return (
    <Host matchContents>
      <HStack spacing={12}>
        <Text>First</Text>
        <Text>Second</Text>
        <Text>Third</Text>
      </HStack>
    </Host>
  );
}
```

### With alignment

The `alignment` prop controls vertical alignment of children. Available options are: `top`, `center`, `bottom`, `firstTextBaseline`, and `lastTextBaseline`.

```tsx
import { Host, HStack, Rectangle } from '@expo/ui/swift-ui';
import { frame } from '@expo/ui/swift-ui/modifiers';

export default function HStackAlignmentExample() {
  return (
    <Host matchContents>
      <HStack spacing={12} alignment="top">
        <Rectangle modifiers={[frame({ width: 50, height: 50 })]} />
        <Rectangle modifiers={[frame({ width: 50, height: 100 })]} />
        <Rectangle modifiers={[frame({ width: 50, height: 75 })]} />
      </HStack>
    </Host>
  );
}
```

## API

```tsx
import { HStack } from '@expo/ui/swift-ui';
```

## Component

### `HStack`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[HStackProps](#hstackprops)\>

HStackProps

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
