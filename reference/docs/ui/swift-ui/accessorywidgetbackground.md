---
title: "AccessoryWidgetBackground"
description: "A SwiftUI adaptive background view that provides a standard appearance based on the the widget's environment."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/accessorywidgetbackground.md"
scraped_at: "2026-07-15T08:59:12.882942"
---

---
title: AccessoryWidgetBackground
description: A SwiftUI adaptive background view that provides a standard appearance based on the the widget's environment.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# AccessoryWidgetBackground

A SwiftUI adaptive background view that provides a standard appearance based on the the widget's environment.
iOS, Included in Expo Go

Expo UI AccessoryWidgetBackground matches the official SwiftUI [AccessoryWidgetBackground API](https://developer.apple.com/documentation/widgetkit/accessorywidgetbackground) and creates an adaptive background view that provides a standard appearance based on the the widget's environment.

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

### Basic accessory widget background

```tsx
import { AccessoryWidgetBackground, VStack, Text, ZStack } from '@expo/ui/swift-ui';

export default function BasicAccessoryWidgetBackground() {
  return (
    <ZStack>
      <AccessoryWidgetBackground />
      <VStack>
        <Text>MON</Text>
      </VStack>
    </ZStack>
  );
}
```

## API

```tsx
import { AccessoryWidgetBackground } from '@expo/ui/swift-ui';
```

## Component

### `AccessoryWidgetBackground`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[AccessoryWidgetBackgroundProps](#accessorywidgetbackgroundprops)\>

AccessoryWidgetBackgroundProps

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
