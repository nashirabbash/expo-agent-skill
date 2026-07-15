---
title: "Box"
description: "A Jetpack Compose Box component for stacking child elements."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/box.md"
scraped_at: "2026-07-15T09:00:40.070857"
---

---
title: Box
description: A Jetpack Compose Box component for stacking child elements.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# Box

A Jetpack Compose Box component for stacking child elements.
Android, Included in Expo Go

Expo UI Box matches the official Jetpack Compose [Box](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#Box) API and stacks children on top of each other with configurable content alignment.

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

`Box` stacks children on top of each other. Use `contentAlignment` to position them within the box.

```tsx
import { Host, Box, Text } from '@expo/ui/jetpack-compose';
import { size, background } from '@expo/ui/jetpack-compose/modifiers';

export default function BoxExample() {
  return (
    <Host matchContents>
      <Box contentAlignment="center" modifiers={[size(200, 200), background('#E0E0E0')]}>
        <Text>Centered in Box</Text>
      </Box>
    </Host>
  );
}
```

## API

```tsx
import { Box } from '@expo/ui/jetpack-compose';
```

## Component

### `Box`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[BoxProps](#boxprops)\>

BoxProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `contentAlignment`

Supported platforms: Android.

Optional • Type: `ContentAlignment`

Alignment of children within the box.

### `floatingToolbarExitAlwaysScrollBehavior`

Supported platforms: Android.

Optional • Type: `FloatingToolbarExitAlwaysScrollBehavior`

Scroll behavior for the floating toolbar exit.

#### Inherited Props

-   `PrimitiveBaseProps`
