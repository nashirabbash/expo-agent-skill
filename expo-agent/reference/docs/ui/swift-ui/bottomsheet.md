---
title: "BottomSheet"
description: "A SwiftUI BottomSheet component that presents content from the bottom of the screen."
source_url: "https://docs.expo.dev/versions/latest/sdk/ui/swift-ui/bottomsheet.md"
scraped_at: "2026-07-15T08:59:14.439531"
---

---
title: BottomSheet
description: A SwiftUI BottomSheet component that presents content from the bottom of the screen.
sourceCodeUrl: 'https://github.com/expo/expo/tree/sdk-57/packages/expo-ui'
packageName: '@expo/ui'
platforms: ['ios', 'tvos', 'expo-go']
---



This documentation is available as Markdown for AI agents and LLMs. See the [full Markdown index](/llms.txt) or append .md to any documentation URL.

# BottomSheet

A SwiftUI BottomSheet component that presents content from the bottom of the screen.
iOS, tvOS, Included in Expo Go

> For cross-platform usage, see the universal [`BottomSheet`](/versions/latest/sdk/ui/universal/bottomsheet.md) — it renders the appropriate native component per platform.

Expo UI BottomSheet matches the official SwiftUI [sheet API](https://developer.apple.com/documentation/swiftui/view/sheet\(ispresented:ondismiss:content:\)) and presents content from the bottom of the screen.

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

### Basic bottom sheet

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Text, VStack } from '@expo/ui/swift-ui';

export default function BasicBottomSheetExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Text>Hello, world!</Text>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet that fits content

Use the [`fitToContents`](/versions/latest/sdk/ui/swift-ui/bottomsheet.md#fittocontents) prop to automatically size the sheet to fit its content.

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Text, VStack } from '@expo/ui/swift-ui';

export default function BottomSheetFitsContentExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented} fitToContents>
          <VStack>
            <Text>This sheet automatically sizes to fit its content.</Text>
            <Button label="Close" onPress={() => setIsPresented(false)} />
          </VStack>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Custom background color

By default, a sheet uses the system's translucent material background (Liquid Glass on iOS 26). Use the [`presentationBackground`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationbackgroundcolor) modifier on `Group` to paint the sheet with a solid color instead, which also opts the sheet out of that translucent material.

> Prefer `presentationBackground` over a `background` modifier on the sheet's content. A `background` sits _behind_ the content's own background, so a `Form` or `List` covers it, and the color shows inconsistently as the sheet moves between detents. `presentationBackground` colors the sheet surface itself, so it stays consistent at every detent. When the content is a `Form` or `List`, also add [`scrollContentBackground('hidden')`](/versions/latest/sdk/ui/swift-ui/modifiers.md#scrollcontentbackgroundvisible) so the sheet color shows through the grouped background.

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Group, Text, VStack } from '@expo/ui/swift-ui';
import {
  presentationBackground,
  presentationDetents,
  padding,
  foregroundStyle,
} from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetBackgroundColorExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(['medium', 'large']),
              presentationBackground('#ffffff'),
            ]}>
            <VStack modifiers={[padding({ all: 20 })]}>
              <Text modifiers={[foregroundStyle('#000000')]}>Solid white sheet background.</Text>
              <Button label="Close" onPress={() => setIsPresented(false)} />
            </VStack>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet with presentation detents

Use the [`presentationDetents`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationdetentsdetents-options) modifier on `Group` to control the available heights. You can use:

-   `'medium'`: System medium height (approximately half screen)
-   `'large'`: System large height (full screen)
-   `{ fraction: number }`: Fraction of screen height (0-1)
-   `{ height: number }`: Fixed height in points

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Group, Text, VStack } from '@expo/ui/swift-ui';
import { presentationDetents } from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetWithDetentsExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(['medium', 'large', { fraction: 0.3 }, { height: 200 }]),
            ]}>
            <Text>This sheet can snap to multiple heights.</Text>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet with detent selection tracking

Pass `selection` and `onSelectionChange` options to [`presentationDetents`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationdetentsdetents-options) to programmatically control which detent the sheet snaps to.

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, List, Section, Text, VStack, Group } from '@expo/ui/swift-ui';
import {
  presentationDetents,
  presentationDragIndicator,
  foregroundStyle,
} from '@expo/ui/swift-ui/modifiers';
import type { PresentationDetent } from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetWithDetentSelectionExample() {
  const [isPresented, setIsPresented] = useState(false);
  const detents: PresentationDetent[] = [{ height: 300 }, { fraction: 0.3 }, 'medium', 'large'];
  const [selectedDetent, setSelectedDetent] = useState<PresentationDetent>('medium');

  const formatDetent = (detent: PresentationDetent): string => {
    if (typeof detent === 'string') return detent;
    if ('fraction' in detent) return `Fraction ${detent.fraction}`;
    return `Height ${detent.height}`;
  };

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Show Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(detents, {
                selection: selectedDetent,
                onSelectionChange: setSelectedDetent,
              }),
              presentationDragIndicator('visible'),
            ]}>
            <List>
              <Section title="Change Detent">
                <Button label="Height 300" onPress={() => setSelectedDetent({ height: 300 })} />
                <Button label="Fraction 0.3" onPress={() => setSelectedDetent({ fraction: 0.3 })} />
                <Button label="Medium" onPress={() => setSelectedDetent('medium')} />
                <Button label="Large" onPress={() => setSelectedDetent('large')} />
              </Section>
              <Section title="Current">
                <Text modifiers={[foregroundStyle('secondaryLabel')]}>
                  {formatDetent(selectedDetent)}
                </Text>
              </Section>
            </List>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet with background interaction

Use the [`presentationBackgroundInteraction`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationbackgroundinteractioninteraction) modifier to allow interactions with content behind the sheet.

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Group, Text, VStack } from '@expo/ui/swift-ui';
import {
  presentationDetents,
  presentationBackgroundInteraction,
} from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetWithBackgroundInteractionExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(['medium', 'large']),
              presentationBackgroundInteraction({ type: 'enabledUpThrough', detent: 'medium' }),
            ]}>
            <Text>Interact with content behind when at medium height.</Text>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Non-dismissible bottom sheet

Use the [`interactiveDismissDisabled`](/versions/latest/sdk/ui/swift-ui/modifiers.md#interactivedismissdisabledisdisabled) modifier to prevent users from dismissing the sheet by swiping.

```tsx
import { useState } from 'react';
import { Host, BottomSheet, Button, Group, Text, VStack } from '@expo/ui/swift-ui';
import { interactiveDismissDisabled } from '@expo/ui/swift-ui/modifiers';

export default function NonDismissibleBottomSheetExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group modifiers={[interactiveDismissDisabled()]}>
            <VStack>
              <Text>This sheet cannot be dismissed by swiping.</Text>
              <Button label="Close" onPress={() => setIsPresented(false)} />
            </VStack>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet with React Native content

Use `RNHostView` to embed React Native components inside the bottom sheet. Set `matchContents` to automatically size the host view to fit its content.

```tsx
import { useState } from 'react';
import { Pressable, Text as RNText, View } from 'react-native';
import { Host, BottomSheet, Button, Group, RNHostView, VStack } from '@expo/ui/swift-ui';
import { presentationDragIndicator } from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetWithRNContentExample() {
  const [isPresented, setIsPresented] = useState(false);
  const [counter, setCounter] = useState(0);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented} fitToContents>
          <Group modifiers={[presentationDragIndicator('visible')]}>
            <RNHostView matchContents>
              <View style={{ padding: 24 }}>
                <RNText style={{ fontSize: 18, fontWeight: 'bold', marginBottom: 8 }}>
                  React Native Content
                </RNText>
                <RNText style={{ color: '#666', marginBottom: 16 }}>Counter: {counter}</RNText>
                <Pressable
                  style={{
                    backgroundColor: '#007AFF',
                    padding: 12,
                    borderRadius: 8,
                    alignItems: 'center',
                    marginBottom: 12,
                  }}
                  onPress={() => setCounter(counter + 1)}>
                  <RNText style={{ color: 'white', fontWeight: '600' }}>Increment</RNText>
                </Pressable>
                <Pressable
                  style={{
                    backgroundColor: '#FF3B30',
                    padding: 12,
                    borderRadius: 8,
                    alignItems: 'center',
                  }}
                  onPress={() => setIsPresented(false)}>
                  <RNText style={{ color: 'white', fontWeight: '600' }}>Close</RNText>
                </Pressable>
              </View>
            </RNHostView>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Bottom sheet with flexible React Native content

When using React Native content with `flex: 1`, omit the `matchContents` prop on `RNHostView` and use [`presentationDetents`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationdetentsdetents-options) to control the sheet height.

```tsx
import { useState } from 'react';
import { Text as RNText, View } from 'react-native';
import { Host, BottomSheet, Button, Group, RNHostView, VStack } from '@expo/ui/swift-ui';
import { presentationDetents, presentationDragIndicator } from '@expo/ui/swift-ui/modifiers';

export default function BottomSheetWithFlexRNContentExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host style={{ flex: 1 }}>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(['medium', 'large']),
              presentationDragIndicator('visible'),
            ]}>
            <RNHostView>
              <View style={{ flex: 1, backgroundColor: '#007AFF', padding: 24 }}>
                <RNText style={{ fontSize: 18, fontWeight: 'bold', color: 'white' }}>
                  Flexible React Native Content
                </RNText>
                <RNText style={{ color: 'white', marginTop: 8 }}>
                  This content fills the available space in the sheet.
                </RNText>
              </View>
            </RNHostView>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

### Scrollable React Native content

Nest a scrollable React Native list such as `FlatList`, `ScrollView`, or a high-performance list like [FlashList](https://shopify.github.io/flash-list/) or [Legend List](https://github.com/LegendApp/legend-list) inside the sheet with `RNHostView`. Size the sheet with [`presentationDetents`](/versions/latest/sdk/ui/swift-ui/modifiers.md#presentationdetentsdetents-options) and the list scrolls within that height.

```tsx
import { useState } from 'react';
import { FlatList, Text as RNText, View } from 'react-native';
import { Host, BottomSheet, Button, Group, RNHostView, VStack } from '@expo/ui/swift-ui';
import { presentationDetents, presentationDragIndicator } from '@expo/ui/swift-ui/modifiers';

const DATA = Array.from({ length: 50 }, (_, i) => `Item ${i + 1}`);

export default function BottomSheetWithScrollableContentExample() {
  const [isPresented, setIsPresented] = useState(false);

  return (
    <Host matchContents>
      <VStack>
        <Button label="Open Sheet" onPress={() => setIsPresented(true)} />
        <BottomSheet isPresented={isPresented} onIsPresentedChange={setIsPresented}>
          <Group
            modifiers={[
              presentationDetents(['medium', 'large']),
              presentationDragIndicator('visible'),
            ]}>
            <RNHostView>
              <View style={{ padding: 16 }}>
                <FlatList
                  data={DATA}
                  keyExtractor={item => item}
                  renderItem={({ item }) => <RNText style={{ paddingVertical: 16 }}>{item}</RNText>}
                />
              </View>
            </RNHostView>
          </Group>
        </BottomSheet>
      </VStack>
    </Host>
  );
}
```

## API

```tsx
import { BottomSheet } from '@expo/ui/swift-ui';
```

## Component

### `BottomSheet`

Supported platforms: iOS, tvOS.

Type: React.Element<[BottomSheetProps](#bottomsheetprops)\>

`BottomSheet` presents content from the bottom of the screen.

BottomSheetProps

### `children`

Supported platforms: iOS, tvOS.

Type: [ReactNode](https://reactnative.dev/docs/react-node)

The children of the `BottomSheet` component. Use `Group` to wrap your content and apply presentation modifiers like `presentationDetents`, `presentationDragIndicator`, `presentationBackgroundInteraction`, and `interactiveDismissDisabled`.

### `fitToContents`

Supported platforms: iOS, tvOS.

Optional • Type: `boolean` • Default: `false`

When `true`, the sheet will automatically size itself to fit its content. This sets the presentation detent to match the height of the children.

### `isPresented`

Supported platforms: iOS, tvOS.

Type: `boolean`

Whether the `BottomSheet` is presented.

### `onDismiss`

Supported platforms: iOS, tvOS.

Optional • Type: `() => void`

Callback function that is called after the `BottomSheet` has been fully dismissed.

### `onIsPresentedChange`

Supported platforms: iOS, tvOS.

Type: `(isPresented: boolean) => void`

Callback function that is called when the `BottomSheet` presented state changes.

#### Inherited Props

-   [CommonViewModifierProps](/versions/latest/sdk/ui/swift-ui/modifiers.md)
