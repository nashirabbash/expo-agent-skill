---
title: "SwipeActions"
description: "A SwiftUI SwipeActions component for adding leading and trailing swipe actions to row content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/swipeactions.md"
scraped_at: "2026-07-15T08:59:09.551805"
---

---
title: SwipeActions
description: A SwiftUI SwipeActions component for adding leading and trailing swipe actions to row content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# SwipeActions

A SwiftUI SwipeActions component for adding leading and trailing swipe actions to row content.
iOS, Included in Expo Go

Expo UI SwipeActions matches the official SwiftUI [swipeActions](https://developer.apple.com/documentation/swiftui/view/swipeactions\(edge:allowsfullswipe:content:\)) modifier and lets you attach leading or trailing actions to row content.

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

```tsx
import { Button, Host, List, Section, SwipeActions, Text } from '@expo/ui/swift-ui';

export default function SwipeActionsExample() {
  return (
    <Host style={{ flex: 1 }}>
      <List>
        <Section>
          <SwipeActions>
            <Text>Message from Expo</Text>

            <SwipeActions.Actions edge="leading" allowsFullSwipe={false}>
              <Button label="Pin" systemImage="pin" onPress={() => {}} />
            </SwipeActions.Actions>

            <SwipeActions.Actions edge="trailing">
              <Button label="Delete" systemImage="trash" role="destructive" onPress={() => {}} />
            </SwipeActions.Actions>
          </SwipeActions>
        </Section>
      </List>
    </Host>
  );
}
```

## API

```tsx
import { SwipeActions } from '@expo/ui/swift-ui';
```

## Components

### `SwipeActions`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SwipeActionsProps](#swipeactionsprops)\>

Applies native SwiftUI swipe actions to its non-slot children.

SwipeActionsProps

### `children`

Supported platforms: iOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The regular content and `SwipeActions.Actions` action groups.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

### `Actions`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[SwipeActionsGroupProps](#swipeactionsgroupprops)\>

The buttons revealed when the user swipes the regular content from an edge.

## Types

### `SwipeActionsEdge`

Supported platforms: iOS.

Literal Type: `string`

Acceptable values are: `'leading'` | `'trailing'`
