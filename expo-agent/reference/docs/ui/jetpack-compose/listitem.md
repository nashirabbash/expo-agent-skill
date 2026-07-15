---
title: "ListItem"
description: "A Jetpack Compose ListItem component for displaying structured list entries."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/jetpack-compose/listitem.md"
scraped_at: "2026-07-15T09:00:40.909969"
---

---
title: ListItem
description: A Jetpack Compose ListItem component for displaying structured list entries.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# ListItem

A Jetpack Compose ListItem component for displaying structured list entries.
Android, Included in Expo Go

Expo UI ListItem matches the official Jetpack Compose [`ListItem`](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary#ListItem\(kotlin.Function0,androidx.compose.ui.Modifier,kotlin.Function0,kotlin.Function0,kotlin.Function0,kotlin.Function0,androidx.compose.material3.ListItemColors,androidx.compose.ui.unit.Dp,androidx.compose.ui.unit.Dp\)) API for structured list entries with headline, supporting, overline, leading, and trailing content slots.

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

### Basic list item

```tsx
import { Host, ListItem, Text } from '@expo/ui/jetpack-compose';

export default function BasicListItem() {
  return (
    <Host matchContents>
      <ListItem>
        <ListItem.HeadlineContent>
          <Text>Settings</Text>
        </ListItem.HeadlineContent>
      </ListItem>
    </Host>
  );
}
```

### With compound components

Use compound components for rich content in each position.

```tsx
import { Host, ListItem, Icon, Text } from '@expo/ui/jetpack-compose';

export default function ListItemWithSlots() {
  return (
    <Host matchContents>
      <ListItem>
        <ListItem.HeadlineContent>
          <Text>Notifications</Text>
        </ListItem.HeadlineContent>
        <ListItem.OverlineContent>
          <Text>ACCOUNT</Text>
        </ListItem.OverlineContent>
        <ListItem.SupportingContent>
          <Text>Manage notification preferences</Text>
        </ListItem.SupportingContent>
        <ListItem.LeadingContent>
          <Icon source={require('./assets/notifications.xml')} />
        </ListItem.LeadingContent>
        <ListItem.TrailingContent>
          <Icon source={require('./assets/chevron.xml')} />
        </ListItem.TrailingContent>
      </ListItem>
    </Host>
  );
}
```

### Clickable list item

Use the `clickable` modifier to handle tap interactions.

```tsx
import { Host, ListItem, Text } from '@expo/ui/jetpack-compose';
import { clickable } from '@expo/ui/jetpack-compose/modifiers';

export default function ClickableListItem() {
  return (
    <Host matchContents>
      <ListItem modifiers={[clickable(() => console.log('Tapped!'))]}>
        <ListItem.HeadlineContent>
          <Text>Tap me</Text>
        </ListItem.HeadlineContent>
      </ListItem>
    </Host>
  );
}
```

### Custom headline content

Use `ListItem.HeadlineContent` for composable headline content like rows with icons.

```tsx
import { Host, ListItem, Text, Row, Icon } from '@expo/ui/jetpack-compose';

export default function ListItemCustomHeadline() {
  return (
    <Host matchContents>
      <ListItem>
        <ListItem.HeadlineContent>
          <Row horizontalArrangement={{ spacedBy: 8 }} verticalAlignment="center">
            <Text>Premium Feature</Text>
            <Icon source={require('./assets/star.xml')} size={16} />
          </Row>
        </ListItem.HeadlineContent>
      </ListItem>
    </Host>
  );
}
```

## API

```tsx
import { ListItem } from '@expo/ui/jetpack-compose';
```

## Component

### `ListItem`

Supported platforms: Android.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ListItemProps](#listitemprops)\>

A list item matching Compose's `ListItem`.

ListItemProps

### `children`

Supported platforms: Android.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Children containing slot sub-components.

### `colors`

Supported platforms: Android.

Optional • Type: [ListItemColors](#listitemcolors)

Colors for list item elements.

### `modifiers`

Supported platforms: Android.

Optional • Type: `ModifierConfig[]`

Modifiers for the component.

### `shadowElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `ListItemDefaults.Elevation`

Shadow elevation in dp.

### `tonalElevation`

Supported platforms: Android.

Optional • Type: `number` • Default: `ListItemDefaults.Elevation`

Tonal elevation in dp.

## Types

### `ListItemColors`

Supported platforms: Android.

Colors for list item elements, matching `ListItemDefaults.colors()`.

| Property | Type | Description |
| --- | --- | --- |
| containerColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| contentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| leadingContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| overlineContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| supportingContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
| trailingContentColor(optional) | [ColorValue](https://reactnative.dev/docs/colors) | - |
