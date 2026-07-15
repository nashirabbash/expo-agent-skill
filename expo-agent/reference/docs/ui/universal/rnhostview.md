---
title: "RNHostView"
description: "A cross-platform component for hosting React Native views inside @expo/ui views."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/rnhostview.md"
scraped_at: "2026-07-15T09:01:45.370283"
---

---
title: RNHostView
description: A cross-platform component for hosting React Native views inside @expo/ui views.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# RNHostView

A cross-platform component for hosting React Native views inside @expo/ui views.
Android, iOS, Web, Included in Expo Go

Hosts a React Native view subtree inside a universal `@expo/ui` layout. On Android and iOS, it re-exports the platform-native [`RNHostView` for Jetpack Compose](/versions/latest/sdk/ui/jetpack-compose/rnhostview.md)/[`RNHostView` for SwiftUI](/versions/latest/sdk/ui/swift-ui/rnhostview.md), so React Native children bridge into the surrounding Compose/SwiftUI tree. On web, there is no native host tree to bridge into, so it falls back to a React Native [`View`](https://reactnative.dev/docs/view) that wraps the children.

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

### Basic usage

Place a React Native view subtree anywhere inside a universal `@expo/ui` layout.

```tsx
import { Host, Column, RNHostView, Text } from '@expo/ui';
import { Text as RNText, View } from 'react-native';

export default function RNHostViewExample() {
  return (
    <Host matchContents>
      <Column spacing={12} style={{ padding: 16 }}>
        <Text textStyle={{ fontWeight: 'bold' }}>Native UI label</Text>
        <RNHostView matchContents>
          <View
            style={{
              alignSelf: 'flex-start',
              padding: 16,
              backgroundColor: '#9B59B6',
              borderRadius: 10,
            }}>
            <RNText style={{ color: 'white' }}>Plain React Native content</RNText>
          </View>
        </RNHostView>
      </Column>
    </Host>
  );
}
```

### Fill parent vs. match child

By default `RNHostView` fills its native parent. Set `matchContents` to have it shrink to fit its React Native children instead.

```tsx
import { Host, Column, Row, Text, RNHostView } from '@expo/ui';
import { View } from 'react-native';

export default function RNHostViewExample() {
  return (
    <Host matchContents>
      <Column spacing={24} style={{ padding: 16 }}>
        <Column spacing={8}>
          <Text textStyle={{ fontSize: 18, fontWeight: 'bold' }}>Fill parent size</Text>
          <Text textStyle={{ fontSize: 12, color: '#666666' }}>
            The RNHostView fills the native parent's 100×100 frame.
          </Text>
          <Row style={{ width: 100, height: 100 }}>
            <RNHostView>
              <View style={{ flex: 1, backgroundColor: '#9B59B6', borderRadius: 10, margin: 4 }} />
            </RNHostView>
          </Row>
        </Column>

        <Column spacing={8}>
          <Text textStyle={{ fontSize: 18, fontWeight: 'bold' }}>Match child size</Text>
          <Text textStyle={{ fontSize: 12, color: '#666666' }}>
            The RNHostView shrinks to wrap its 50×50 child.
          </Text>
          <Row style={{ padding: 8 }}>
            <RNHostView matchContents>
              <View
                style={{ width: 50, height: 50, backgroundColor: '#9B59B6', borderRadius: 10 }}
              />
            </RNHostView>
          </Row>
        </Column>
      </Column>
    </Host>
  );
}
```

## API

```tsx
import { RNHostView } from '@expo/ui';
```

## Component

### `RNHostView`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[RNHostViewProps](#rnhostviewprops)\>

Hosts React Native views inside Jetpack Compose or SwiftUI views.

Props for the [`RNHostView`](#rnhostview) component.

RNHostViewProps

### `children`

Supported platforms: Android, iOS, Web.

Type: `ReactElement`

The React Native view to host.

### `disabled`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is disabled. Disabled components do not respond to user interaction.

### `hidden`

Supported platforms: Android, iOS, Web.

Optional • Type: `boolean`

Whether the component is hidden.

### `matchContents`

Supported platforms: Android, iOS.

Optional • Type: `boolean` • Default: `false`

When `true`, the host updates its size in the native view tree to match the children's size. When `false`, the host uses the size of the parent native view.

Can only be set once on mount; changing it remounts the component.

### `modifiers`

Supported platforms: Android, iOS.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. A modifier supplied here replaces any modifier of the same type that the component derives from `style` or other props.

### `onAppear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component appears on screen.

### `onDisappear`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is removed from screen.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Called when the component is pressed.

### `style`

Supported platforms: Android, iOS, Web.

Optional • Type: [Pick](https://www.typescriptlang.org/docs/handbook/utility-types.html#picktype-keys)<[ViewStyle](https://reactnative.dev/docs/view-style-props), 'padding' | 'paddingHorizontal' | 'paddingVertical' | 'paddingTop' | 'paddingBottom' | 'paddingLeft' | 'paddingRight' | 'backgroundColor' | 'borderRadius' | 'borderWidth' | 'borderColor' | 'opacity' | 'width' | 'height'\>

Platform-agnostic style properties. These are translated to SwiftUI modifiers on iOS and Jetpack Compose modifiers on Android.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.
