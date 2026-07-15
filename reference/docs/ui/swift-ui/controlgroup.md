---
title: "ControlGroup"
description: "A SwiftUI ControlGroup component for grouping interactive controls."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/controlgroup.md"
scraped_at: "2026-07-15T08:59:21.780951"
---

---
title: ControlGroup
description: A SwiftUI ControlGroup component for grouping interactive controls.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ControlGroup

A SwiftUI ControlGroup component for grouping interactive controls.
iOS, tvOS, Included in Expo Go

Expo UI ControlGroup matches the official SwiftUI [ControlGroup API](https://developer.apple.com/documentation/swiftui/controlgroup). When placed inside a [`Menu`](/versions/latest/sdk/ui/swift-ui/menu.md), the children are rendered as a compact horizontal row of buttons.

> **Note:** On tvOS, `ControlGroup` requires tvOS 17.0 or later.

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

### Basic control group

A control group inside a menu, these render as a horizontal row of icon buttons.

```tsx
import { Host, Menu, ControlGroup, Button } from '@expo/ui/swift-ui';

export default function BasicControlGroupExample() {
  return (
    <Host matchContents>
      <Menu label="Options" systemImage="ellipsis.circle">
        <ControlGroup>
          <Button systemImage="plus" label="Add" onPress={() => console.log('Add')} />
          <Button systemImage="star" label="Favorite" onPress={() => console.log('Favorite')} />
          <Button
            systemImage="square.and.arrow.up"
            label="Share"
            onPress={() => console.log('Share')}
          />
        </ControlGroup>
        <Button label="Other Action" onPress={() => console.log('Other')} />
      </Menu>
    </Host>
  );
}
```

## API

```tsx
import { ControlGroup } from '@expo/ui/swift-ui';
```

## Component

### `ControlGroup`

Supported platforms: iOS, tvOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ControlGroupProps](#controlgroupprops)\>

ControlGroupProps

### `children`

Supported platforms: iOS, tvOS 17.0+.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The control group's content. Can contain `Button`, `Toggle`, `Picker`, or other interactive controls.

### `label`

Supported platforms: iOS 16.0+, tvOS 17.0+.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The label for the control group. Can be a string for simple text labels, or a `Label` component for custom label content. When omitted, the control group has no label.

### `systemImage`

Supported platforms: iOS 16.0+, tvOS 17.0+.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

An SF Symbol name to display alongside the label. Only used when `label` is a string.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
