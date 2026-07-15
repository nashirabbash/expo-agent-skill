---
title: "Overlay"
description: "A SwiftUI Overlay component for layering content on top of another view."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/overlay.md"
scraped_at: "2026-07-15T08:59:44.051885"
---

---
title: Overlay
description: A SwiftUI Overlay component for layering content on top of another view.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvOS', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Overlay

A SwiftUI Overlay component for layering content on top of another view.
iOS, tvOS, Included in Expo Go

Expo UI Overlay matches the official SwiftUI [overlay](https://developer.apple.com/documentation/swiftui/view/overlay\(alignment:content:\)) modifier and provides a way to layer secondary content on top of a view, positioned with a specified alignment.

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
import { Host, Overlay, Text, Image } from '@expo/ui/swift-ui';
import {
  foregroundStyle,
  frame,
  font,
  background,
  clipShape,
  offset,
} from '@expo/ui/swift-ui/modifiers';

export default function OverlayExample() {
  return (
    <Host style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Overlay alignment="topTrailing">
        <Image
          systemName="bell.fill"
          modifiers={[font({ size: 28 }), foregroundStyle('#007AFF')]}
        />
        <Overlay.Content>
          <Text
            modifiers={[
              font({ size: 11, weight: 'bold' }),
              foregroundStyle('#FFFFFF'),
              frame({ width: 18, height: 18 }),
              background('#FF3B30'),
              clipShape('circle'),
              offset({ x: 8, y: -8 }),
            ]}>
            3
          </Text>
        </Overlay.Content>
      </Overlay>
    </Host>
  );
}
```

## API

```tsx
import { Overlay } from '@expo/ui/swift-ui';
```

## Component

### `Overlay`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[OverlayProps](#overlayprops)\>

OverlayProps

### `alignment`

Supported platforms: iOS, tvOS.

Optional • Type: [Alignment](#alignment) • Default: `'center'`

The alignment of the overlay content relative to the base content.

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
