---
title: "Divider"
description: "A SwiftUI Divider component for creating visual separators."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/divider.md"
scraped_at: "2026-07-15T08:59:12.046090"
---

---
title: Divider
description: A SwiftUI Divider component for creating visual separators.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Divider

A SwiftUI Divider component for creating visual separators.
iOS, tvOS, Included in Expo Go

Expo UI Divider matches the official SwiftUI [Divider API](https://developer.apple.com/documentation/swiftui/divider) and creates a visual separator between content.

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

### Basic divider

```tsx
import { Host, Divider, VStack, Text } from '@expo/ui/swift-ui';

export default function BasicDividerExample() {
  return (
    <Host matchContents>
      <VStack>
        <Text>First section</Text>
        <Divider />
        <Text>Second section</Text>
      </VStack>
    </Host>
  );
}
```

### Divider in a list

```tsx
import { Host, Divider, VStack, Text } from '@expo/ui/swift-ui';

export default function DividerInListExample() {
  return (
    <Host matchContents>
      <VStack spacing={8}>
        <Text>Item 1</Text>
        <Divider />
        <Text>Item 2</Text>
        <Divider />
        <Text>Item 3</Text>
        <Divider />
        <Text>Item 4</Text>
      </VStack>
    </Host>
  );
}
```

### Divider in a context menu

Dividers are commonly used to separate groups of actions in context menus.

```tsx
import { Host, ContextMenu, Button, Text, Divider } from '@expo/ui/swift-ui';

export default function DividerInContextMenuExample() {
  return (
    <Host matchContents>
      <ContextMenu>
        <ContextMenu.Items>
          <Button label="Edit" onPress={() => console.log('Edit')} />
          <Button label="Duplicate" onPress={() => console.log('Duplicate')} />
          <Divider />
          <Button label="Delete" role="destructive" onPress={() => console.log('Delete')} />
        </ContextMenu.Items>
        <ContextMenu.Trigger>
          <Text>Long press me</Text>
        </ContextMenu.Trigger>
      </ContextMenu>
    </Host>
  );
}
```

## API

```tsx
import { Divider } from '@expo/ui/swift-ui';
```

## Component

### `Divider`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[DividerProps](#dividerprops)\>

Divider component uses the native [Divider](https://developer.apple.com/documentation/swiftui/divider) component. A visual element that can be used to separate other content.

DividerProps

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
