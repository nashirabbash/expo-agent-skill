---
title: "Popover"
description: "A SwiftUI Popover component for displaying content in a floating overlay."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/popover.md"
scraped_at: "2026-07-15T08:59:29.277297"
---

---
title: Popover
description: A SwiftUI Popover component for displaying content in a floating overlay.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Popover

A SwiftUI Popover component for displaying content in a floating overlay.
iOS, Included in Expo Go

Expo UI Popover matches the official SwiftUI [Popover API](https://developer.apple.com/documentation/swiftui/view/popover\(ispresented:attachmentanchor:arrowedge:content:\)) and provides a way to present content in a floating overlay anchored to a trigger element.

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

### Basic popover

```tsx
import { useState } from 'react';
import { Host, Button, Popover, Text, VStack } from '@expo/ui/swift-ui';
import { padding } from '@expo/ui/swift-ui/modifiers';

export default function BasicPopoverExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Popover
        isPresented={isPresented}
        onStateChange={({ isPresented }) => setIsPresented(isPresented)}>
        <Popover.Trigger>
          <Button label="Show Popover" onPress={() => setIsPresented(true)} />
        </Popover.Trigger>
        <Popover.Content>
          <VStack modifiers={[padding({ all: 16 })]}>
            <Text>Hello from Popover!</Text>
          </VStack>
        </Popover.Content>
      </Popover>
    </Host>
  );
}
```

### With attachment anchor

The `attachmentAnchor` prop controls where the popover attaches to the trigger element. Available options are: `center`, `leading`, `trailing`, `top`, and `bottom`.

```tsx
import { useState } from 'react';
import { Host, Button, Popover, Text, VStack } from '@expo/ui/swift-ui';
import { padding } from '@expo/ui/swift-ui/modifiers';

export default function AttachmentAnchorExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Popover
        isPresented={isPresented}
        onStateChange={({ isPresented }) => setIsPresented(isPresented)}
        attachmentAnchor="trailing">
        <Popover.Trigger>
          <Button label="Show Popover" onPress={() => setIsPresented(true)} />
        </Popover.Trigger>
        <Popover.Content>
          <VStack modifiers={[padding({ all: 16 })]}>
            <Text>Attached to trailing edge</Text>
          </VStack>
        </Popover.Content>
      </Popover>
    </Host>
  );
}
```

### With arrow edge

The `arrowEdge` prop controls which edge of the popover displays the arrow. Available options are: `none`, `leading`, `trailing`, `top`, and `bottom`.

```tsx
import { useState } from 'react';
import { Host, Button, Popover, Text, VStack } from '@expo/ui/swift-ui';
import { padding } from '@expo/ui/swift-ui/modifiers';

export default function ArrowEdgeExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <Popover
        isPresented={isPresented}
        onStateChange={({ isPresented }) => setIsPresented(isPresented)}
        arrowEdge="top">
        <Popover.Trigger>
          <Button label="Show Popover" onPress={() => setIsPresented(true)} />
        </Popover.Trigger>
        <Popover.Content>
          <VStack modifiers={[padding({ all: 16 })]}>
            <Text>Arrow on top edge</Text>
          </VStack>
        </Popover.Content>
      </Popover>
    </Host>
  );
}
```

### With React Native content

You can use `RNHostView` to embed React Native components inside the popover content.

```tsx
import { useState } from 'react';
import { Pressable, Text as RNText, View } from 'react-native';
import { Host, Button, Popover, RNHostView } from '@expo/ui/swift-ui';

export default function RNContentPopoverExample() {
  const [isPresented, setIsPresented] = useState(false);
  const [counter, setCounter] = useState(0);

  return (
    <Host matchContents>
      <Popover
        isPresented={isPresented}
        onStateChange={({ isPresented }) => setIsPresented(isPresented)}>
        <Popover.Trigger>
          <Button label="Show RN Popover" onPress={() => setIsPresented(true)} />
        </Popover.Trigger>
        <Popover.Content>
          <RNHostView matchContents>
            <View style={{ padding: 16 }}>
              <RNText style={{ fontSize: 16, fontWeight: 'bold' }}>React Native Content</RNText>
              <RNText style={{ color: '#666', marginVertical: 8 }}>Counter: {counter}</RNText>
              <Pressable
                style={{
                  backgroundColor: '#007AFF',
                  padding: 12,
                  borderRadius: 8,
                  alignItems: 'center',
                }}
                onPress={() => setCounter(counter + 1)}>
                <RNText style={{ color: 'white' }}>Increment</RNText>
              </Pressable>
            </View>
          </RNHostView>
        </Popover.Content>
      </Popover>
    </Host>
  );
}
```

## API

```tsx
import { Popover } from '@expo/ui/swift-ui';
```

## Component

### `Popover`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[PopoverViewProps](#popoverviewprops)\>

## Props

### `arrowEdge`

Supported platforms: iOS.

Optional • Literal type: `string` • Default: `'none'`

The edge of the `attachmentAnchor` that defines the location of the popover's arrow. The default is `none`, which results in the system allowing any arrow edge.

Acceptable values are: `'none'` | `'top'` | `'bottom'` | `'leading'` | `'trailing'`

### `attachmentAnchor`

Supported platforms: iOS.

Optional • Literal type: `string`

The positioning anchor that defines the attachment point of the popover.

Acceptable values are: `'center'` | `'top'` | `'bottom'` | `'leading'` | `'trailing'`

### `children`

Supported platforms: iOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `isPresented`

Supported platforms: iOS.

Optional • Type: `boolean`

Whether the popover is presented.

### `onIsPresentedChange`

Supported platforms: iOS.

Optional • Type: `(isPresented: boolean) => void`

A callback that is called when the `isPresented` state changes.

### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
