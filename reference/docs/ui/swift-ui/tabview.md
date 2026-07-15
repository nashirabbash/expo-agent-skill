---
title: "TabView"
description: "A SwiftUI TabView component for paged or tabbed content."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/tabview.md"
scraped_at: "2026-07-15T08:59:34.360014"
---

---
title: TabView
description: A SwiftUI TabView component for paged or tabbed content.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# TabView

A SwiftUI TabView component for paged or tabbed content.
iOS, tvOS, Included in Expo Go

Expo UI TabView matches the official SwiftUI [TabView API](https://developer.apple.com/documentation/swiftui/tabview) and switches between styles via the [`tabViewStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#tabviewstyleconfig) modifier.

> **Note:** For routed bottom-tab navigation across full-screen routes, use [`expo-router/unstable-native-tabs`](/router/advanced/native-tabs.md) instead.

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

Each page is a `<TabView.Tab>` child, identified by a `value` prop. `TabView` does not impose its own height — give it a frame, or place it inside a parent that does.

### Page style (swipeable pager)

Use `tabViewStyle({ type: 'page' })` for a horizontal pager with optional dot indicators. Pass `defaultSelection` to start the pager on a specific page without controlling it from React.

```tsx
import { Host, Spacer, TabView, Text, VStack } from '@expo/ui/swift-ui';
import {
  background,
  font,
  foregroundStyle,
  frame,
  tabViewStyle,
} from '@expo/ui/swift-ui/modifiers';

const fillFrame = frame({ maxWidth: Infinity, maxHeight: Infinity });
const pageFrame = frame({ minHeight: 320, maxHeight: 320 });

export default function PagerExample() {
  return (
    <Host style={{ flex: 1 }}>
      <TabView defaultSelection="1" modifiers={[pageFrame, tabViewStyle({ type: 'page' })]}>
        <TabView.Tab value="0">
          <Page label="Page 1" color="#6200EE" />
        </TabView.Tab>
        <TabView.Tab value="1">
          <Page label="Page 2" color="#03DAC5" />
        </TabView.Tab>
        <TabView.Tab value="2">
          <Page label="Page 3" color="#FF5722" />
        </TabView.Tab>
      </TabView>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <VStack alignment="center" modifiers={[fillFrame, background(color)]}>
      <Spacer />
      <Text modifiers={[font({ size: 28, weight: 'bold' }), foregroundStyle('#FFFFFF')]}>
        {label}
      </Text>
      <Spacer />
    </VStack>
  );
}
```

### Controlled selection

Pass `selection` and `onSelectionChange` to drive the active tab from React state. Each `<TabView.Tab>`'s `value` is matched against `selection`. Add the [`animation`](/versions/latest/sdk/ui/swift-ui/modifiers.md#animationanimation-value) modifier to animate transitions when `selection` changes from JS.

```tsx
import { useState } from 'react';
import { Button, Host, Spacer, TabView, Text, VStack } from '@expo/ui/swift-ui';
import {
  animation,
  Animation,
  background,
  font,
  foregroundStyle,
  frame,
  tabViewStyle,
} from '@expo/ui/swift-ui/modifiers';

const fillFrame = frame({ maxWidth: Infinity, maxHeight: Infinity });
const pageFrame = frame({ minHeight: 320, maxHeight: 320 });

export default function ControlledTabViewExample() {
  const [selected, setSelected] = useState('0');

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Text>Selected: {selected}</Text>
        <Button label="Go to page 3" onPress={() => setSelected('2')} />
        <TabView
          selection={selected}
          onSelectionChange={setSelected}
          modifiers={[
            pageFrame,
            tabViewStyle({ type: 'page' }),
            animation(Animation.default, Number(selected)),
          ]}>
          <TabView.Tab value="0">
            <Page label="Page 1" color="#6200EE" />
          </TabView.Tab>
          <TabView.Tab value="1">
            <Page label="Page 2" color="#03DAC5" />
          </TabView.Tab>
          <TabView.Tab value="2">
            <Page label="Page 3" color="#FF5722" />
          </TabView.Tab>
        </TabView>
      </VStack>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <VStack alignment="center" modifiers={[fillFrame, background(color)]}>
      <Spacer />
      <Text modifiers={[font({ size: 28, weight: 'bold' }), foregroundStyle('#FFFFFF')]}>
        {label}
      </Text>
      <Spacer />
    </VStack>
  );
}
```

### Page indicator dots

Use the [`indexViewStyle`](/versions/latest/sdk/ui/swift-ui/modifiers.md#indexviewstyleconfig) modifier together with `tabViewStyle({ type: 'page' })` to control the dot indicators. Set `indexDisplayMode` to `'always'`, `'never'`, or `'automatic'`, and `backgroundDisplayMode` to render a translucent pill behind the dots.

```tsx
import { Host, Spacer, TabView, Text, VStack } from '@expo/ui/swift-ui';
import {
  background,
  font,
  foregroundStyle,
  frame,
  indexViewStyle,
  tabViewStyle,
} from '@expo/ui/swift-ui/modifiers';

const fillFrame = frame({ maxWidth: Infinity, maxHeight: Infinity });
const pageFrame = frame({ minHeight: 320, maxHeight: 320 });

export default function PageIndicatorExample() {
  return (
    <Host style={{ flex: 1 }}>
      <TabView
        modifiers={[
          pageFrame,
          tabViewStyle({ type: 'page', indexDisplayMode: 'always' }),
          indexViewStyle({ backgroundDisplayMode: 'always' }),
        ]}>
        <TabView.Tab value="0">
          <Page label="Page 1" color="#4F8DF6" />
        </TabView.Tab>
        <TabView.Tab value="1">
          <Page label="Page 2" color="#34C759" />
        </TabView.Tab>
        <TabView.Tab value="2">
          <Page label="Page 3" color="#FF9F0A" />
        </TabView.Tab>
      </TabView>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <VStack alignment="center" modifiers={[fillFrame, background(color)]}>
      <Spacer />
      <Text modifiers={[font({ size: 28, weight: 'bold' }), foregroundStyle('#FFFFFF')]}>
        {label}
      </Text>
      <Spacer />
    </VStack>
  );
}
```

### Bottom tab bar

Use `tabViewStyle({ type: 'automatic' })` for the SwiftUI default tab bar. Each tab's `label` and `systemImage` populate the bar item. Use the [`badge`](/versions/latest/sdk/ui/swift-ui/modifiers.md#badgevalue) modifier on a tab to attach a badge to its bar item.

> **Note:** For routed bottom-tab navigation across full-screen routes, use [`expo-router/unstable-native-tabs`](/router/advanced/native-tabs.md) instead.

```tsx
import { useState } from 'react';
import { Host, Spacer, TabView, Text, VStack } from '@expo/ui/swift-ui';
import {
  background,
  badge,
  font,
  foregroundStyle,
  frame,
  tabViewStyle,
} from '@expo/ui/swift-ui/modifiers';

const fillFrame = frame({ maxWidth: Infinity, maxHeight: Infinity });

export default function BottomTabsExample() {
  const [selected, setSelected] = useState('inbox');

  return (
    <Host style={{ flex: 1 }}>
      <TabView
        selection={selected}
        onSelectionChange={setSelected}
        modifiers={[tabViewStyle({ type: 'automatic' })]}>
        <TabView.Tab value="inbox" label="Inbox" systemImage="tray.fill" modifiers={[badge('3')]}>
          <Page label="Inbox" color="#4F8DF6" />
        </TabView.Tab>
        <TabView.Tab value="sent" label="Sent" systemImage="paperplane.fill">
          <Page label="Sent" color="#34C759" />
        </TabView.Tab>
        <TabView.Tab value="drafts" label="Drafts" systemImage="square.and.pencil">
          <Page label="Drafts" color="#FF9F0A" />
        </TabView.Tab>
      </TabView>
    </Host>
  );
}

function Page({ label, color }: { label: string; color: string }) {
  return (
    <VStack alignment="center" modifiers={[fillFrame, background(color)]}>
      <Spacer />
      <Text modifiers={[font({ size: 28, weight: 'bold' }), foregroundStyle('#FFFFFF')]}>
        {label}
      </Text>
      <Spacer />
    </VStack>
  );
}
```

## API

```tsx
import { TabView } from '@expo/ui/swift-ui';
```

## Component

### `TabView`

Supported platforms: iOS.

Type: React.[Element](https://www.typescriptlang.org/docs/handbook/jsx.html#function-component)<[TabViewProps](#tabviewprops)\>

A SwiftUI `TabView`. Pair with modifiers to choose the appearance:

-   `tabViewStyle({ type: 'page' })` — swipeable pager.
-   `tabViewStyle({ type: 'automatic' })` — bottom tab bar.
-   `tabViewStyle({ type: 'sidebarAdaptable' })` — sidebar on iPad, tab bar on iPhone.

Use `<TabView.Tab>` children to define pages. Each tab is identified by its `value` prop, which is used for selection.

For routed bottom-tab navigation across full-screen routes, prefer `expo-router/unstable-native-tabs`.

TabViewProps

### `children`

Supported platforms: iOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The tab's content — rendered when this tab is selected.

### `label`

Supported platforms: iOS.

Optional • Type: `string`

Text label shown in the tab bar or sidebar.

### `systemImage`

Supported platforms: iOS.

Optional • Type: [SFSymbols7_0](https://github.com/nandorojo/sf-symbols-typescript)

SF Symbol name shown alongside the label.

### `value`

Supported platforms: iOS.

Type: `string`

Identifies this tab. Matched against the parent `TabView`'s `selection` and `defaultSelection` props.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)

### `children`

Supported platforms: iOS.

Literal type: `union`

`<TabView.Tab>` elements defining the pages.

Acceptable values are: `ReactElement<unknown, string | JSXElementConstructor<any>>` | `ReactElement[]`

### `defaultSelection`

Supported platforms: iOS.

Optional • Type: `string`

The initially selected tab when the component is uncontrolled (no `selection` prop). Ignored if `selection` is provided.

### `onSelectionChange`

Supported platforms: iOS.

Optional • Type: `(selection: string) => void`

Called when the selected tab changes.

### `selection`

Supported platforms: iOS.

Optional • Type: `string`

The selected tab (controlled mode). Pair with `onSelectionChange`. Pass `defaultSelection` instead to let the native view manage state.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
