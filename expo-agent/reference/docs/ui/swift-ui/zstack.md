---
title: "ZStack"
description: "A SwiftUI ZStack component for overlapping layouts."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/zstack.md"
scraped_at: "2026-07-15T08:59:13.787103"
---

---
title: ZStack
description: A SwiftUI ZStack component for overlapping layouts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ZStack

A SwiftUI ZStack component for overlapping layouts.
iOS, tvOS, Included in Expo Go

Expo UI ZStack matches the official SwiftUI [ZStack API](https://developer.apple.com/documentation/swiftui/zstack) and overlays its children on top of each other.

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

### Basic overlapping stack

```tsx
import { Host, ZStack, Rectangle, Text } from '@expo/ui/swift-ui';
import { frame, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function BasicZStackExample() {
  return (
    <Host matchContents>
      <ZStack>
        <Rectangle modifiers={[frame({ width: 100, height: 100 })]} />
        <Text modifiers={[foregroundStyle('white')]}>Overlay</Text>
      </ZStack>
    </Host>
  );
}
```

### With alignment

The `alignment` prop controls how children are positioned within the stack. Available options include: `center`, `leading`, `trailing`, `top`, `bottom`, `topLeading`, `topTrailing`, `bottomLeading`, and `bottomTrailing`.

```tsx
import { Host, ZStack, Rectangle, Circle } from '@expo/ui/swift-ui';
import { frame, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function ZStackAlignmentExample() {
  return (
    <Host matchContents>
      <ZStack alignment="bottomTrailing">
        <Rectangle modifiers={[frame({ width: 100, height: 100 }), foregroundStyle('blue')]} />
        <Circle modifiers={[frame({ width: 30, height: 30 }), foregroundStyle('red')]} />
      </ZStack>
    </Host>
  );
}
```

### Creating a badge overlay

```tsx
import { Host, ZStack, Circle, Text, Image } from '@expo/ui/swift-ui';
import { frame, foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function ZStackBadgeExample() {
  return (
    <Host matchContents>
      <ZStack alignment="topTrailing">
        <Image systemName="bell.fill" size={32} color="blue" />
        <Circle modifiers={[frame({ width: 16, height: 16 }), foregroundStyle('red')]} />
      </ZStack>
    </Host>
  );
}
```

## API

```tsx
import { ZStack } from '@expo/ui/swift-ui';
```

## Component

### `ZStack`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ZStackProps](#zstackprops)\>

ZStackProps

### `alignment`

Supported platforms: iOS, tvOS.

Optional • Type: [Alignment](#alignment)

The alignment of children within the stack.

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
