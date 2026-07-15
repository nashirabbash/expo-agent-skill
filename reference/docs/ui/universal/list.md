---
title: "List"
description: "A virtualized vertical container of rows, paired with a tappable ListItem primitive."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/universal/list.md"
scraped_at: "2026-07-15T09:01:39.446884"
---

---
title: List
description: A virtualized vertical container of rows, paired with a tappable ListItem primitive.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['android', 'ios', 'web', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# List

A virtualized vertical container of rows, paired with a tappable ListItem primitive.
Android, iOS, Web, Included in Expo Go

`List` provides a virtualized vertical container of rows, typically populated with [`ListItem`](/versions/latest/sdk/ui/universal/list.md#listitem) children. It provides the platform-native chrome (separators, inset styling, pull-to-refresh).`ListItem` is a tappable row with `leading`/`trailing`/`supportingText` slots.

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

### Basic list

```tsx
import { useState } from 'react';
import { Host, List, ListItem, Text } from '@expo/ui';

const ITEMS = [
  { id: 1, name: 'Avocado toast' },
  { id: 2, name: 'Bagel with cream cheese' },
  { id: 3, name: 'Cappuccino' },
];

export default function ListExample() {
  const [selected, setSelected] = useState<string | null>(null);

  return (
    <Host style={{ flex: 1 }}>
      <List>
        {ITEMS.map(item => (
          <ListItem key={item.id} onPress={() => setSelected(item.name)}>
            {item.name}
          </ListItem>
        ))}
      </List>
      {selected != null && <Text>Selected: {selected}</Text>}
    </Host>
  );
}
```

### Rows with slots

`ListItem` accepts `leading`, `trailing`, and `supportingText` shorthand props for the common case. Pass a `ReactNode` for any of them when richer content is needed.

```tsx
import { Host, Icon, List, ListItem } from '@expo/ui';

const CHEVRON = Icon.select({
  ios: 'chevron.right',
  android: require('@expo/material-symbols/chevron_right.xml'),
});

export default function ListItemSlotsExample() {
  return (
    <Host style={{ flex: 1 }}>
      <List>
        <ListItem
          onPress={() => {}}
          trailing={<Icon name={CHEVRON} size={14} color="gray" />}
          supportingText="Secondary line below the headline">
          Profile
        </ListItem>
        <ListItem onPress={() => {}} trailing={<Icon name={CHEVRON} size={14} color="gray" />}>
          Settings
        </ListItem>
      </List>
    </Host>
  );
}
```

### Compound slot children

For full control over slot content, use the compound API: `<ListItem.Leading>`, `<ListItem.Trailing>`, and `<ListItem.Supporting>`. Anything not wrapped in a slot becomes the headline.

```tsx
import { Host, Icon, List, ListItem, Row, Text } from '@expo/ui';

export default function ListItemCompoundExample() {
  return (
    <Host style={{ flex: 1 }}>
      <List>
        <ListItem onPress={() => {}}>
          <ListItem.Leading>
            <Icon name="star.fill" size={20} color="#FFD60A" />
          </ListItem.Leading>
          <Row spacing={0}>
            <Text textStyle={{ color: 'gray' }}>{`#42: `}</Text>
            <Text>Composite headline</Text>
          </Row>
          <ListItem.Supporting>Richer slot content</ListItem.Supporting>
        </ListItem>
      </List>
    </Host>
  );
}
```

### Pull-to-refresh

Pass an `async` `onRefresh` handler. The platform-native refresh indicator stays visible until the returned promise settles (resolves or rejects).

```tsx
import { useState } from 'react';
import { Host, List, ListItem } from '@expo/ui';

export default function ListRefreshExample() {
  const [items, setItems] = useState([1, 2, 3]);

  const handleRefresh = async () => {
    await new Promise(resolve => setTimeout(resolve, 1500));
    setItems(prev => [Math.max(...prev) + 1, ...prev]);
  };

  return (
    <Host style={{ flex: 1 }}>
      <List onRefresh={handleRefresh}>
        {items.map(id => (
          <ListItem key={id}>{`Item #${id}`}</ListItem>
        ))}
      </List>
    </Host>
  );
}
```

> Pull-to-refresh is not implemented on web yet. The handler is accepted for API parity but the indicator only appears on Android and iOS.

## API

```tsx
import { List, ListItem } from '@expo/ui';
```

## Component

### `List`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ListProps](#listprops)\>

A vertical container of rows. Typically populated with [`ListItem`](#listitem) children.

Props for the [`List`](#list) component. A virtualized vertical container of rows. Typically populated with [`ListItem`](#listitem) children, though any node is accepted.

ListProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

The list rows. Usually `<ListItem>` elements.

### `onRefresh`

Supported platforms: Android, iOS.

Optional • Type: () => [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)<void\>

Optional pull-to-refresh handler. When provided, the list shows the platform-native refresh affordance. The returned promise drives the indicator's visibility.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

## Components

### `ListItem`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[ListItemProps](#listitemprops)\>

A tappable row in a list. Composes with [`List`](#list). Pass row content via the `leading` / `trailing` / `supportingText` shorthand props or the compound `<ListItem.Leading>` / `<ListItem.Trailing>` / `<ListItem.Supporting>` slot children.

Props for the [`ListItem`](#listitem) component. A tappable row in a list.

ListItemProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Headline content of the row. The remaining (non-slot) children are rendered in the headline area.

### `leading`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Shorthand for the leading slot. Overridden by `<ListItem.Leading>` if both are provided.

### `modifiers`

Supported platforms: Android, iOS, Web.

Optional • Type: `ModifierConfig[]`

Platform-specific modifier escape hatch. Pass an array of modifier configs from `@expo/ui/swift-ui/modifiers` or `@expo/ui/jetpack-compose/modifiers`. On iOS these are applied to the underlying SwiftUI `Button` and can override its default `buttonStyle(.plain)`.

### `onPress`

Supported platforms: Android, iOS, Web.

Optional • Type: `() => void`

Tap handler. Activates over the entire row rectangle, including the empty gap between leading/headline/trailing.

### `supportingText`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Shorthand for the supporting (sub-)text slot. Strings are rendered with platform-appropriate secondary styling; pass a `ReactNode` for richer content. Overridden by `<ListItem.Supporting>` if both are provided.

### `testID`

Supported platforms: Android, iOS, Web.

Optional • Type: `string`

Identifier used to locate the component in end-to-end tests.

### `trailing`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Shorthand for the trailing slot. Overridden by `<ListItem.Trailing>` if both are provided.

### `ListItem.Leading`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[ListItemLeadingProps](#listitemleadingprops)\>\>

Props for the [`ListItem.Leading`](#listitemleading) slot marker.

ListItemLeadingProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered in the leading (start) slot.

### `ListItem.Supporting`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[ListItemSupportingProps](#listitemsupportingprops)\>\>

Props for the [`ListItem.Supporting`](#listitemsupporting) slot marker.

ListItemSupportingProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered below the headline.

### `ListItem.Trailing`

Supported platforms: Android, iOS, Web.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<FC<[ListItemTrailingProps](#listitemtrailingprops)\>\>

Props for the [`ListItem.Trailing`](#listitemtrailing) slot marker.

ListItemTrailingProps

### `children`

Supported platforms: Android, iOS, Web.

Optional • Type: [ReactNode](https://reactnative.dev/docs/react-node)

Content rendered in the trailing (end) slot.
