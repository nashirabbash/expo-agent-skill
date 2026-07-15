---
title: "FlowRow"
description: "A Jetpack Compose FlowRow component for wrapping children horizontally."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/flowrow.md"
scraped_at: "2026-07-15T09:00:25.428645"
---

---
title: FlowRow
description: A Jetpack Compose FlowRow component for wrapping children horizontally.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# FlowRow

A Jetpack Compose FlowRow component for wrapping children horizontally.
Android, Included in Expo Go

Expo UI FlowRow matches the official Jetpack Compose [FlowRow](https://developer.android.com/reference/kotlin/androidx/compose/foundation/layout/package-summary#FlowRow) API and arranges children in a horizontal flow that wraps to the next line when it runs out of space.

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

`FlowRow` arranges children in a horizontal flow that wraps to the next line when it runs out of space.

```tsx
import { Host, FlowRow, Text } from '@expo/ui/jetpack-compose';
import { paddingAll } from '@expo/ui/jetpack-compose/modifiers';

export default function FlowRowExample() {
  const tags = ['React Native', 'Expo', 'Android', 'Jetpack Compose', 'Material 3', 'Kotlin'];

  return (
    <Host matchContents>
      <FlowRow
        horizontalArrangement={{ spacedBy: 8 }}
        verticalArrangement={{ spacedBy: 8 }}
        modifiers={[paddingAll(16)]}>
        {tags.map(tag => (
          <Text key={tag}>{tag}</Text>
        ))}
      </FlowRow>
    </Host>
  );
}
```

## API

```tsx
import { FlowRow } from '@expo/ui/jetpack-compose';
```

## Component

### `FlowRow`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[FlowRowProps](#flowrowprops)\>

FlowRowProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

### `horizontalArrangement`

Supported platforms: Android.

Optional • Type: `HorizontalArrangement`

Horizontal arrangement of children.

### `verticalArrangement`

Supported platforms: Android.

Optional • Type: `VerticalArrangement`

Vertical arrangement of children.

#### Inherited Props

-   `PrimitiveBaseProps`
