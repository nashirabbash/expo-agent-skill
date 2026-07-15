---
title: "Group"
description: "A SwiftUI Group component for grouping views without affecting layout."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/group.md"
scraped_at: "2026-07-15T08:59:22.416583"
---

---
title: Group
description: A SwiftUI Group component for grouping views without affecting layout.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Group

A SwiftUI Group component for grouping views without affecting layout.
iOS, tvOS, Included in Expo Go

Expo UI Group matches the official SwiftUI [Group API](https://developer.apple.com/documentation/swiftui/group) and groups views together without introducing additional layout structure.

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

### Basic group

Groups are useful for applying modifiers to multiple views at once or organizing views without affecting layout.

```tsx
import { Host, Group, Text } from '@expo/ui/swift-ui';
import { foregroundStyle } from '@expo/ui/swift-ui/modifiers';

export default function BasicGroupExample() {
  return (
    <Host matchContents>
      <Group modifiers={[foregroundStyle('blue')]}>
        <Text>First item</Text>
        <Text>Second item</Text>
        <Text>Third item</Text>
      </Group>
    </Host>
  );
}
```

## API

```tsx
import { Group } from '@expo/ui/swift-ui';
```

## Component

### `Group`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[GroupProps](#groupprops)\>

GroupProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
