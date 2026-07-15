---
title: "Spacer"
description: "A SwiftUI Spacer component for flexible spacing."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/spacer.md"
scraped_at: "2026-07-15T08:59:42.577891"
---

---
title: Spacer
description: A SwiftUI Spacer component for flexible spacing.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Spacer

A SwiftUI Spacer component for flexible spacing.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`Spacer`](/versions/latest/sdk/ui/universal/spacer.md) — it renders the appropriate native component per platform.

Expo UI Spacer matches the official SwiftUI [Spacer API](https://developer.apple.com/documentation/swiftui/spacer) and expands to fill available space in a stack.

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

### Basic spacer in HStack

Use Spacer to push content to opposite ends of a horizontal stack.

```tsx
import { Host, HStack, Text, Spacer } from '@expo/ui/swift-ui';

export default function SpacerHStackExample() {
  return (
    <Host style={{ flex: 1 }}>
      <HStack>
        <Text>Left</Text>
        <Spacer />
        <Text>Right</Text>
      </HStack>
    </Host>
  );
}
```

### Basic spacer in VStack

Use Spacer to push content to opposite ends of a vertical stack.

```tsx
import { Host, VStack, Text, Spacer } from '@expo/ui/swift-ui';

export default function SpacerVStackExample() {
  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Text>Top</Text>
        <Spacer />
        <Text>Bottom</Text>
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { Spacer } from '@expo/ui/swift-ui';
```

## Component

### `Spacer`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SpacerProps](#spacerprops)\>

SpacerProps

### `minLength`

Supported platforms: iOS, tvOS.

Optional • Type: `number`

The minimum length of the spacer. This is the minimum amount of space that the spacer will take up.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
